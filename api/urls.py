from django.urls import path
from .views import LastProductsList

urlpatterns = [
    path('last-products',LastProductsList.as_view())
]
