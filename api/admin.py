from django.contrib import admin
from django.utils.html import format_html

from .models import Category,Product,Color,Tag,Size

admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Tag)

class SizeInline(admin.TabularInline):
    model = Product.size.through
    extra = 1
    min_num = 1
    max_num = 4

class ColorInline(admin.TabularInline):
    model = Product.color.through
    extra = 1
    min_num = 0
    max_num = 5
    fields = ['color']

class TagInline(admin.TabularInline):
    model = Product.tag.through
    extra = 1
    min_num = 0
    max_num = 3

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ColorInline,SizeInline,TagInline]

    list_display = ['title', 'ref', 'category', 'oldPrice', 'newPrice', 'stock', 'created']
    list_filter = ['category', 'created']
    search_fields = ['title', 'ref', 'brand']
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Informations', {
            'fields': ('title','brand','category','slug','ref')
        }),
        ('Prix et promotion', {
            'fields': ('oldPrice','percent','newPrice')
        }),
        ('Stock et garantie', {
           'fields': ('stock', 'warranty') 
        }),
        ('Images', {
            'fields': ('imgDefault', 'imgHover')
        }),
        ('Description', {
            'fields': ('description',)
        })
    )
    readonly_fields = ['ref', 'newPrice']

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_dispaly = ['value','color_preview','get_products_count']
    search_fields = ['value']

    def color_preview(self,obj):
        if obj.value.startswith('#'):
            return format_html(
                '<div style="with: 30px;height:30px;background:{};border: 1px solid #ccc;"></div>',
                obj.value
            )
        return obj.value
    color_preview.short_description = 'Aperçu'