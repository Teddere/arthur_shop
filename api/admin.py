from django.contrib import admin
from django.utils.html import format_html

from .models import Category,Product,Color,Tag,Size,Badge

admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Tag)
admin.site.register(Badge)

class SizeInline(admin.TabularInline):
    model = Product.size.through
    extra = 1
    min_num = 1
    max_num = 5

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
    max_num = 5


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ColorInline,SizeInline,TagInline]

    list_display = ['title', 'ref', 'category', 'oldPrice', 'newPrice', 'stock', 'created','badge']
    list_filter = ['category', 'created']
    search_fields = ['title', 'ref', 'brand']
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Informations', {
            'fields': ('title','brand','category','badge','slug','ref')
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
    list_dispaly = ['value','color_preview']
    search_fields = ['value']

    def color_preview(self,obj):
        if obj.value.startswith('#'):
            return format_html(
                '<div style="with: 30px;height:30px;background:{};border: 1px solid #ccc;"></div>',
                obj.value
            )
        return obj.value
    color_preview.short_description = 'Aperçu'