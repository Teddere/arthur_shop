from django.db import models
from django.utils.text import slugify

from .utils import discount_val,generate_ref


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True,null=True)
    thumbnail = models.ImageField(upload_to='categories/',null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

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


class Size(models.Model):
    
    class SizeChoices(models.TextChoices):
        xxs = 'XXS','xxs'
        xs = 'XS','xs'
        s = 'S','s'
        m = 'M','m'
        l = 'L','l'
        xl = 'XL','xl'
        xxl = 'XXL','xxl'
        size_0 = '36','36'
        size_1 = '37','37'
        size_2 = '38','38'
        size_3 = '39','39'
        size_4 = '40','40'
        size_5 = '41','41'
        size_6 = '42','42'
        size_7 = '43','43'
        size_8 = '44','44'
        size_9 = '45','45'
        
    code = models.CharField(max_length=10,choices=SizeChoices,unique=True)

    class Meta:
        db_table = 'sizes'
        verbose_name = 'Taille'
        verbose_name_plural = 'Tailles'
        ordering = ['code']

    def __str__(self):
        return f"{self.code}"

class Color(models.Model):
    name = models.CharField(max_length=20,blank=True,null=True)
    value = models.CharField(max_length=15,blank=True)

    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    name = models.CharField(max_length=20,unique=True)

    class Meta:
        db_table = 'tags'
        verbose_name = 'Etiquette'
        verbose_name_plural = 'Etiquettes'
    
    def __str__(self):
        return f"{self.name}"

class Badge(models.Model):
    class BadgeChoices(models.TextChoices):
        badge = 'Promo'
        badge_0 = 'Collection'
        badge_1 = 'Nouveau'
        badge_2 = 'Edition'
    class classChoices(models.TextChoices):
        pink = 'light-pink'
        blue = 'light-blue'
        green = 'light-green'
        orange = 'light-orange'
    name = models.CharField(max_length=20,choices=BadgeChoices, blank=True,null=True)
    className = models.CharField(max_length=20,choices=classChoices,blank=True,null=True)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    title = models.CharField(max_length=150)
    ref = models.CharField(max_length=10,blank=True,null=True)
    slug = models.SlugField(unique=True,blank=True,max_length=50)

    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    size = models.ManyToManyField(Size)
    tag = models.ManyToManyField(Tag)
    color = models.ManyToManyField(Color)
    badge = models.ForeignKey(Badge,on_delete=models.Empty,blank=True,null=True)
    brand = models.CharField(max_length=100,blank=True,null=True)
    percent = models.IntegerField(blank=True,null=True)
    newPrice = models.DecimalField(blank=True,null=True,decimal_places=2, max_digits=10)
    oldPrice = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField(default=0)
    warranty = models.IntegerField(blank=True,null=True)

    imgDefault = models.ImageField(upload_to='products/',blank=True,null=True)
    imgHover = models.ImageField(upload_to='products/',blank=True,null=True)

    description = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return f"/{self.category.slug}/{self.slug}/"
    
    def get_image_default(self):
        if (self.imgDefault) :
            return f"http://127.0.0.1:8000{self.imgDefault.url}"
        return ''
        
    def get_image_hover(self):
        if self.imgHover:
            return f"http://127.0.0.1:8000{self.imgHover.url}"
        return ''
    

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.ref:
            self.ref = generate_ref()
        if self.percent:
            self.newPrice = discount_val(self.oldPrice,self.percent)
        return super().save(*args,**kwargs)