from django.urls import path
from order import views

app_name = 'order'

urlpatterns = [
    path('checkout/',views.checkout), #checkout
    path('orders/',views.OrdersList.as_view()) #order_list
]
