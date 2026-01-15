from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product,Category,Badge
from .serializers import ProductSerializer,ProductDetailSerializer,CategoryDetailSerializer


class CategoryList(APIView):
    def get(self,request,format=None):
        categories = Category.objects.all()[:10]
        serializer = CategoryDetailSerializer(categories,many=True)
        return Response(serializer.data)
class CategoryListSelect(APIView):
    def get_object_select(self,category_name):
        try:
            product = Product.objects.filter(category__name=category_name)
            return product
        except Product.DoesNotExist:
            raise Http404
    
    def get(self,request,category_slug,format=None):
        product = self.get_object_select(category_slug)
        serializer = ProductSerializer(product,many=True)
        return Response(serializer.data)

class CategoryDetailSelect(APIView):
    def get_object_select(self,category_slug):
        try:
            product = Product.objects.filter(category__slug=category_slug)[:5]
            return product
        except Product.DoesNotExist:
            raise Http404
    def get(self,request,category_slug):
        products = self.get_object_select(category_slug)
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)

class ProductList(APIView):
    def get(self,request,format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)

class ProductListSelect(APIView):
    def get_object_select(self,badge):
        try:
            product = Product.objects.filter(badge__name=badge)[:10]
            return product
        except Product.DoesNotExist:
            raise Http404
        
    def get(self,request,format=None):

        saleProducts = self.get_object_select(Badge.BadgeChoices.badge)
        newProducts = self.get_object_select(Badge.BadgeChoices.badge_1)
        editProducts = self.get_object_select(Badge.BadgeChoices.badge_2)
        data = [
            {'name':'new','products':ProductSerializer(newProducts,many=True).data},
            {'name':'sale','products':ProductSerializer(saleProducts,many=True).data},
            {'name':'edit','products':ProductSerializer(editProducts,many=True).data}
        ]
        return Response(data)

class LastProductsList(APIView):
    def get(self,request,format=None):
        products = Product.objects.all()[:8]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self,category_slug,product_slug):
        try:
           prod = Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
           return prod
        except Product.DoesNotExist:
            raise Http404

    def get(self,request,category_slug,product_slug,format=None):
        product = self.get_object(category_slug,product_slug)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)
