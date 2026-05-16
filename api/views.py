from django.http import Http404
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product,Category,Badge
from .serializers import ProductSerializer,ProductDetailSerializer,CategoryDetailSerializer

# recupération de toutes les catégories
class CategoryList(APIView):
    def get(self,request,format=None):
        categories = Category.objects.all()
        serializer = CategoryDetailSerializer(categories,many=True)
        return Response(serializer.data)
# catégorie sélectionnée
class CategoryListSelect(APIView):
    def get_object_select(self,category_slug):
        try:
            product = Product.objects.filter(category__slug=category_slug)
            return product
        except Product.DoesNotExist:
            raise Http404
    
    def get(self,request,category_slug,format=None):
        product = self.get_object_select(category_slug)
        serializer = ProductSerializer(product,many=True)
        return Response(serializer.data)
# catégorie associée au detail product
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
# recupération de tous les products
class ProductList(APIView):
    def get(self,request,format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
# recupération de article de navigation (home page)
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
# recupépation des derniers articles
class LastProductsList(APIView):
    def get(self,request,format=None):
        products = Product.objects.all()[:8]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
# recupération d'article détaillé 
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
# recherche de product(s)
@api_view(['POST'])
def search(request):
    query = request.data.get("query",'')
    if query:
        products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    else:
        return Response({"products":[]})



