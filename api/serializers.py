from rest_framework import serializers
from .models import Category, Product, Badge, Color, Size,Tag

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
        fields = ('name','value')
# Size
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('code',)
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)
# resume product
class ProductSerializer(serializers.ModelSerializer):
    badge = BadgeSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = (
            'title',
            'badge',
            'category',
            'newPrice',
            'oldPrice',
            'color',
            'stock',
            'get_image_default',
            'get_image_hover',
            'get_absolute_url',
        )

# Detail product
class ProductDetailSerializer(ProductSerializer):
    badge = BadgeSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    size = SizeSerializer(many=True,read_only=True)
    color = ColorSerialize(many=True,read_only=True)
    tag = TagSerializer(many=True,read_only=True)
    class Meta:
        model = Product
        fields = (
            'title',
            'ref',
            'brand',
            'percent',
            'size',
            'stock',
            'tag',
            'color',
            'warranty',
            'newPrice',
            'oldPrice',
            'description',
            'get_image_default',
            'get_image_hover',
            'get_absolute_url',
        )





