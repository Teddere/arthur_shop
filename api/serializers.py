from rest_framework import serializers
from .models import Category, Product, Badge

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)
class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ('id','name','className')
class ProductSerializer(serializers.ModelSerializer):
    badge = BadgeSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = (
            'ref',
            'title',
            'badge',
            'category',
            'newPrice',
            'oldPrice',
            'stock',
            'get_image_default',
            'get_image_hover',
            'get_absolute_url',
        )




