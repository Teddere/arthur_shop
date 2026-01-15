from django.urls import path
from api import views

app_name = 'api'
urlpatterns = [
    path('categories/',views.CategoryList.as_view(),name='category_all'),
    path('categories/<slug:category_slug>',views.CategoryListSelect.as_view()),
    path('categories/detail/<slug:category_slug>/',views.CategoryDetailSelect.as_view(),name='category_detail'),
    path('products/all/',views.ProductList.as_view(),name='product_all'),
    path('products/selected/',views.ProductListSelect.as_view(),name='product_select'),
    path('last-products/',views.LastProductsList.as_view(),name='last-products'),
    path('products/<slug:category_slug>/<slug:product_slug>/',views.ProductDetail.as_view(),name='product'),
]
