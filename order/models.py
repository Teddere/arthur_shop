from django.contrib.auth.models import User
from django.db import models
from api.models import Product


class Order(models.Model):
    user = models.ForeignKey(User,related_name='orders',on_delete=models.CASCADE)
    paid_amount = models.DecimalField(max_digits=15,decimal_places=2,null=True,blank=True)
    stripe_token = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100,null=True,blank=True)
    comment = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.first_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15,decimal_places=2)
    quantity = models.ImageField(default=1)

    def __str__(self):
        return '%s' % self.id # type: ignore
    



