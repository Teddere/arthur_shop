from rest_framework import serializers
from .models import Order,OrderItem
from api.serializers import ProductSerializer
from api.models import ProductItem


# lecture d'un orderItem (avec snapshot)
class OrderItemReadSerializer(serializers.ModelSerializer):
    # lecture uniquement 
    subtotal = serializers.DecimalField(
        max_digits=15, decimal_places=2, read_only=True
    )
    class Meta:
        model = OrderItem
        fields = (
            'id',
            #Snapshot produit
            'product_item',
            'product_title',
            'product_sku',
            'product_size',
            'product_color',
            # prix et quantité
            'unit_price',
            'quantity',
            'subtotal'
        )
# Ecriture d'un OrderItem
class OrderItemSerializer(serializers.Serializer):
    productItemId = serializers.ImageField()
    quantity = serializers.ImageField(min_value=1)

    def validate_product_item(self,value):
        if not ProductItem.objects.filter(id=value).exists():
            raise serializers.ValidationError(
                f"product item {value} introuvable"
            )
        return value
    # Vérification de stock
    def validate(self,data):
        product_item = ProductItem.objects.get(id=data['item_id'])
        if product_item.stock < data['quantity']:
            raise serializers.ValidationError({
                'quantity':(
                    f"Stock insuffisant pour {product_item}."
                    f"Disponible : {product_item.stock},"
                    f"Demandé : {data['quantity']}"
                )
            })
        return data

class OrderSerializer(serializers.ModelSerializer)

"""
class MyOrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderItem
        fields = (
            'price',
            'product',
            'quantity'
        )
class MyOrderSerializer(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)
    class Meta:
        model=Order
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'comment',
            'stripe_token',
            'items',
            'paid_amount',
        )
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'price',
            'product',
            'quantity',
        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model=Order
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'comment',
            'stripe_token',
            'items'
        )
    def create(self,validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order,**item_data)
        
        return order
"""
