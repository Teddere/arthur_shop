from rest_framework import serializers
from .models import Category, Product, ProductItem,Badge, Color, Size,Tag

# Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)
# Badge
class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ('id','name','className')
# Color
class ColorSerialize(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('name','color')
# Size
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('code',)
# Tag
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)
# productItem
class ProductItemSerializer(serializers.ModelSerializer):
    size = serializers.StringRelatedField()
    color =  ColorSerialize(read_only=True)
    is_available = serializers.BooleanField(read_only=True)
    base_price = serializers.DecimalField(max_digits=10,decimal_places=2,read_only=True)

    class Meta:
        model = ProductItem
        fields = (
            'id',
            'sku',
            'size',
            'color',
            'newPrice',
            'percent',
            'stock',
            'stock_status',
            'base_price',
            'is_available',
        )


# resume product
class ProductSerializer(serializers.ModelSerializer):
    badge = BadgeSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    is_available = serializers.BooleanField(read_only=True)
    element = serializers.SerializerMethodField()
    image_default = serializers.SerializerMethodField()
    image_hover = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'badge',
            'category',
            'price',
            'description',
            'is_available',
            'element',
            'image_default',
            'image_hover',
            'url',
        )
    def get_element(self,obj):
        items = ProductItem.objects.filter(
            product=obj
        ).select_related('size')
        items_in_stock = items.filter(stock__gt=0)
        # Si aucun item en stock, on prend tous les items (affichage rupture)
        pool = items_in_stock if items_in_stock.exists() else items

        if not pool.exists():
            return None
        #items avec newPrice parmi le pool
        items_discount = pool.filter(newPrice__isnull=False)
        if items_discount.exists():
            product = items_discount.order_by('newPrice').first()
        else:
            product = min(
                pool,
                key=lambda item: item.oldPrice if item.oldPrice is not None else obj.price
            )
        if not product:
            return None

        return {
            'id': product.id,
            'sku': product.sku,
            'size': product.size.code if product.size else None,
            'color': {'name': product.color.name,'value': product.color.color} if product.color else None,
            'stock': product.stock,
            'stock_status': product.stock_status,
            'is_available': product.is_available,
            'base_price': product.base_price,
            'newPrice': product.newPrice,
            'percent': product.percent,

        }
    def get_image_default(self, obj):
        return obj.get_image_default()
    def get_image_hover(self, obj):
        return obj.get_image_hover()
    def get_url(self,obj):
        return obj.get_absolute_url()


# Detail product
class ProductDetailSerializer(ProductSerializer):
    tag = TagSerializer(many=True,read_only=True)
    size_list = serializers.SerializerMethodField()
    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + (
            'ref',
            'tag',
            'brand',
            'warranty',
            'size_list',
            'description',
        )
    def get_size_list(self,obj):
        items = (
            ProductItem.objects
            .filter(product=obj)
            .select_related('size','color')
        )
        sizes = {}
        for item in items:
            size_code = item.size.code if item.size else 'Unique'
            sizes.setdefault(size_code, {
                'size': size_code,
                'in_stock': False,
                'items': []
            })
            sizes[size_code]['items'].append({
                'product_item_id': item.id,
                'sku': item.sku,
                'color': { 'name': item.color.name, 'value': item.color.color } if item.color else None,
                'stock': item.stock,
                'stock_status': item.stock_status,
                'is_available': item.is_available,
                'percent': item.percent,
                'base_price': item.base_price,
                'newPrice': item.newPrice if item.newPrice else None,
            })
            if item.is_available:
                sizes[size_code]['in_stock'] = True
        sorted_size = sorted(sizes.values(), key=lambda s: sort_sizes(s['size']))
        return sorted_size


def sort_sizes(size_code):
    SIZE_ORDER = [
        'XXS','XS','S','M','L','XL','XXL',
        '36','37','38','39','40','41','42',
        '43','44','45'
    ]
    try:
        return SIZE_ORDER.index(size_code.upper())
    except ValueError:
        return len(SIZE_ORDER)

# Category
class CategoryDetailSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    image_category = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = (
            'name',
            'slug',
            'image_category',
            'url'
        )
    def get_image_category(self,obj):
        return obj.get_image_category()
    def get_url(self,obj):
        return obj.get_absolute_url()



