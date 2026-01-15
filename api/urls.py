from django.urls import path
from api import views

app_name = 'api'
urlpatterns = [
    path('last-products/',views.LastProductsList.as_view(),name='last-products'),
    path('products/<slug:category_slug>/<slug:product_slug>/',views.ProductDetail.as_view(),name='product'),
]
