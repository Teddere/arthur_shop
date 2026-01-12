from django.db import models
from django.utils.text import slugify

from .utils import discount_val,generate_ref


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True,null=True)
    thumbnail = models.ImageField(upload_to='categories/',null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Catégories"
        verbose_name = "Catégorie"

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)


class Product(models.Model):
    name = models.CharField(max_length=150)
    ref = models.CharField(max_length=10,blank=True,null=True)
    slug = models.SlugField(unique=True,blank=True,max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.CharField(max_length=100,blank=True,null=True)
    percent = models.IntegerField(blank=True,null=True)
    newPrice = models.DecimalField(blank=True,null=True,decimal_places=2, max_digits=10)
    oldPrice = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField(default=0)
    warranty = models.IntegerField(blank=True,null=True)
    imgDefault = models.ImageField(upload_to='products/',blank=True,null=True)
    imgHover = models.ImageField(upload_to='products/',blank=True,null=True)
    description = models.TextField(blank=True,null=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            self.ref = generate_ref()
        if self.percent:
            self.newPrice = discount_val(self.oldPrice,self.percent)

        return super().save(*args,**kwargs)

class Size(models.Model):
    SIZE_CHOICES = ['XS','S','M','L','XL','XXL']
    code = models.TextChoices(value=SIZE_CHOICES)
    product = models.ManyToManyField(Product)

    class Meta:
        db_name = 'sizes'
        verbose_name = 'Taille'
        verbose_name_plural = 'Tailles'
        ordering = ['code']

    def __str__(self):
        return f"{self.code}"

class Color(models.Model):
    value = models.CharField(max_length=15,blank=True,null=True)
    product = models.ManyToManyField(Product,blank=True,null=True)


class Tag(models.Model):
    name = models.CharField(max_length=20,unique=True)
    product = models.ManyToManyField(Product,blank=True,null=True)

    class Meta:
        db_table = 'tags'
        verbose_name = 'Etiquette'
        verbose_name_plural = 'Etiquettes'
    
    def __str__(self):
        return f"{self.name}"

