from django.urls import path
from api import views

app_name = 'api'
urlpatterns = [
    # recupération de toutes les catégories
    path('categories/',views.CategoryList.as_view(),name='category_all'),
    # catégorie sélectionnée
    path('catalog/<slug:category_slug>/',views.CategoryListSelect.as_view()),
    # catégorie associée au detail product
    path('categories/detail/<slug:category_slug>/',views.CategoryDetailSelect.as_view(),name='category_detail'),
    # recupération de tous les products
    path('products/all/',views.ProductList.as_view(),name='product_all'),
    # recupération de article de navigation (home page)
    path('products/selected/',views.ProductListSelect.as_view(),name='product_select'),
    # recherche de product(s)
    path('products/search/',views.search,name='product_search'),
    # recupépation des derniers articles
    path('last-products/',views.LastProductsList.as_view(),name='last-products'),
    # recupération d'article détaillé 
    path('products/<slug:category_slug>/<slug:product_slug>/',views.ProductDetail.as_view(),name='product'),
]
