from django.urls import path
from api import views

urlpatterns = [
    path('last-products/',views.LastProductsList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/',views.ProductDetail.as_view())
]
