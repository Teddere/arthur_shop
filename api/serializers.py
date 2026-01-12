from rest_framework import serializers
from .models import Category,Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = {
            'id',
            'ref',
            'slug',
            'brand',
            'percent',
            'newPrice',
            'oldPrice',
            'warranty',
            'stock',
            'get_image_default',
            'get_image_hover',
            'get_absolute_url',
        }

