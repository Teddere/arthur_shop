from rest_framework import serializers
from django.db import transaction
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
    productItem = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

    def validate_product_item(self,value):
        if not ProductItem.objects.filter(id=value).exists():
            raise serializers.ValidationError(
                f"produit  introuvable"
            )
        return value
    # Vérification de stock
    def validate(self,data):
        product_item = ProductItem.objects.get(id=data['productItem'])
        if product_item.stock < data['quantity']:
            raise serializers.ValidationError({
                'quantity':(
                    f"Stock insuffisant pour {product_item}."
                    f"Disponible : {product_item.stock},"
                    f"Demandé : {data['quantity']}"
                )
            })
        return data

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
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
    @transaction.atomic
    def create(self,validated_data):
        items_data = validated_data.pop('items')
# public stripe key validated_data('stripe_token,value)
        order = Order.objects.create(**validated_data)

        for item in items_data:
# évite une vente e double si on a deux ventes en même temps
            product_item = ProductItem.objects.select_for_update().get(id=item['productItem'])
            quantity = item['quantity']
            # check quantity in stoc
            if (product_item.stock < quantity):
                raise serializers.ValidationError(
                    f'Stock insuffisant pour {product_item.product.title}'
                )

            unit_price = product_item.newPrice or product_item.base_price

            OrderItem.objects.create(
                order=order,
                product_title = product_item.product.title,
                product_sku = product_item.sku,
                product_size = product_item.size.code,
                product_color = product_item.color.name,
                unit_price = unit_price,
                quantity = quantity
                )
            product_item.stock -= quantity
            product_item.save(update_fields=['stock'])

        return order


class MyOrderSerializer(serializers.ModelSerializer):
    items = OrderItemReadSerializer(many=True,read_only=True)
    class Meta:
        model = Order
        fields = (
            'id',
            'ref',
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'paid_amount',
            'items',
            'created'
        )
