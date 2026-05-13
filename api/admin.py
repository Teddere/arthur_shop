from idlelib.colorizer import color_config

from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Product, ProductItem, Tag, Size, Badge, Color

admin.site.register(Size)
admin.site.register(Tag)
admin.site.register(Badge)


#------- Category --------------------------------------------#

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','thumbnail']
    search_fields = ['name']
    prepopulated_fields = {'slug':('name',)}

#------- Color --------------------------------------------#

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'color','color_preview']
    search_fields = ['name','color']
    def color_preview(self, obj):
        if obj.color:
            return format_html(
                '<div style="width:30px;height:30px;background:{};border:'
                '1px solid #ccc;border-radius:4px;></div>"',
                obj.color
            )
        return '-'
    color_preview.short_description = 'Aperçu'

#----- ProductItem Inline in product ----------------------#
class ProductItemInline(admin.TabularInline):
    model = ProductItem
    extra = 1
    min_num = 1
    readonly_fields = ['newPrice','sku','stock_status','finalPrice']
    fields = ['size','color','sku','stock','stock_status','low_stock','oldPrice','newPrice','percent' ]
# ------ read only properties -----------------------------#
    def stock_status(self,obj):
        colors = {
            'in_stock':('✅','#2d6a4f'),
            'low_stock':('⚠️','#b7770d'),
            'out_of_stock':('❌','#c0392b'),
        }
        icon,color = colors.get(obj.stock_status,('-','#000'))

        return format_html(
            '<span style="color:{}">{} {}</span>',
            color,icon,obj.stock_status
        )
    stock_status.short_description= 'Statut stock'

    def finalPrice(self,obj):
        if obj.newPrice:
            return format_html(
                '<span style="text-decoration:line-through;color:#999">{} €</span>'
                '&nbsp;<strong style="color:#C0392B">{} €</strong>'
                '&nbsp;<span style="color:#2D6A4F">-{}%</span>',
                obj.base_price,obj.newPrice,obj.percent
            )
        return format_html(
            '<strong>{} €</strong>',
            obj.base_price
        )
    finalPrice.short_description = 'Prix final'


#------ Product --------------------------------------------#
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductItemInline]
    readonly_fields = ['ref','total_stock','is_available']
    list_display = ['title','badge','brand','price','warranty','imgDefault','imgHover','description']
    list_filter = ['category','badge','brand','created']
    search_fields = ['title','ref','brand']
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Informations article', {
            'fields':('title','brand','category','badge','tag','slug')
        }),
        ('Prix de référence', {
            'fields':('price','warranty'),
            'description': 'Le prix de référence sert de base à toutes les variantes'
        }),
        ('Images', {
            'fields': ('imgDefault','imgHover')
        }),
        ('Description', {
            'fields':('description',)
        }),
        ('Stock global', {
            'fields':('total_stock','is_available'),
            'description': 'Calculé automatiquement depuis les déclinaisons'
        })
    )

    def total_stock(self,obj):
        stock = obj.total_stock
        color = '#2d6a4f' if stock > 0 else '#c0392b'
        return format_html(
            '<strong style="color:{}">{}</strong>',
            color,stock
        )
    total_stock.short_description = 'Stock total'

    def is_available(self,obj):
        if obj.is_available:
            return format_html('<span style="color:#2d6a4">✅ Disponible</span>')
        return format_html('<span style="color:#c0392b">❌ Rupture</span>')
    is_available.short_description = 'Is available'
    is_available.boolean = False
