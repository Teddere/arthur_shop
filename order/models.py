from django.contrib.auth import get_user_model
from django.db import models
from api.models import ProductItem

from .utils import _generate_ref

User = get_user_model()

class Order(models.Model):
    class StatusChoices(models.TextChoices):
        pending = 'pending', 'En attente'
        confirmed = 'confirmed', 'Confirmée'
        shipped = 'shipped', 'Expédiée'
        delivered = 'delivered', 'Livrée'
        cancelled = 'cancelled', 'Annulée'
        refounded = 'refunded', 'Remboursée'
    
    class PaymentChoices(models.TextChoices):
        pending = 'pending', 'En attente'
        paid = 'paid', 'Payé'
        failed = 'failed', 'Échoué'
        refunded = 'refunded', 'Remboursé'

    user = models.ForeignKey(User,related_name='orders',on_delete=models.SET_NULL,null=True,blank=True)
    # référence 
    ref = models.CharField(max_length=20,unique=True,blank=True)
    # status
    status = models.CharField(max_length=20,choices=StatusChoices,default=StatusChoices.pending)
    paymenet_status = models.CharField(
        max_length=20,choices=PaymentChoices,default=PaymentChoices.pending
    )
    # paiement
    paid_amount = models.DecimalField(max_digits=15,decimal_places=2,null=True,blank=True)
    stripe_token = models.CharField(max_length=100)
    # information client
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    comment = models.TextField(null=True,blank=True)
    # Adresse de livraison
    address = models.CharField(max_length=100,null=True,blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Commande'
        verbose_name_plural = 'Commandes'
    
    def __str__(self):
        return f"Commande {self.ref} - {self.first_name} {self.last_name}"
    # total calculé depuis orderItem
    @property
    def total(self):
        return sum(item.subtotal for item in self.items.all())
    # Nombre d'articles
    @property
    def total_items(self):
        return sum(item.quantity for item in self.items.all())
    
    def save(self,*args,**kwargs):
        if not self.ref:
            self.ref = _generate_ref()
        super().save(*args,**kwargs)



class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    # prductItem 
    product_item = models.ForeignKey(
        ProductItem, related_name='order_items',on_delete=models.SET_NULL,null=True
    )
    # snapshot au moment de la commande
    # Ces champs preservent les données même si le produit est modifié
    product_title = models.CharField(max_length=150)
    product_sku = models.CharField(max_length=50)
    product_size = models.CharField(max_length=10,blank=True,null=True)
    product_color = models.CharField(max_length=20, blank=True, null=True)

    #Prix au moment de l'achat (ne doit jamais changer après)
    unit_price = models.DecimalField(max_digits=15,decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Article commandé'
        verbose_plural = 'Articles commandés'
    
    def __str__(self):
        return f"{self.product_title} X{self.quantity} ({self.product_sku})"
    
    @property
    def subtotal(self):
        return self.unit_price * self.quantity
    
    @classmethod
    def from_cart_item(cls,order,product_item,quantity):
        return cls (
            order = order,
            product_item = product_item,
            product_title = product_item.product.title,
            product_sku = product_item.sku,
            product_size = product_item.size.code if product_item.size else None,
            product_color = product_item.color.name if product_item.color else None,
            unit_price = product_item.newPrice if product_item.newPrice else product_item.base_price
        )

    



