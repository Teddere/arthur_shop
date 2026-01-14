import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arthur.settings')
import django
django.setup()
from api.models import Product,Category,Size,Color,Badge,Tag

from faker import Faker

def populate_category_table():
    
    liste = [
        {'id':1,'name':'Sneakers','image':'images/snearkes.png'},
        {'id':2,'name':'T-shirt','image':'images/t-shirt.png'},
        {'id':3,'name':'Chaussure','image':'images/shoes-11.png'},
        {'id':4,'name':'Manteaux','image':'images/coat-4.png'},
        {'id':5,'name':'Chemise','image':'images/shirt.png'},
        {'id':6,'name':'Pull','image':'images/pull-1.png'},
        {'id':7,'name':'Short','image':'images/short.png'},
        {'id':8,'name':'Sac','image':'images/bag-5.png'},
        {'id':9,'name':'Accessoire','image':'images/banner_pub.jpg'},
        {'id':10,'name':'Costume','image':'images/suit.png'},
        {'id':11,'name':'Montre','image':'images/watch-5.png'},
       ]

    for item in liste:
        Category.objects.create(
            name = item['name'],
            thumbnail = item['image']
        )

def populate_size_table():
    liste = ['XS','S','M','L','XL','XXL','36','37','38','39','40','41','42','43','44','45']
    for size in liste:
        Size.objects.create(
            code = size
        )

def populate_color_table():
    liste = [
        {'id':1,'name':'blanc','hex':'#ffffff'},
        {'id':2,'name':'noir','hex':'#000000'},
        {'id':3,'name':'gris','hex':'#808080'},
        {'id':4,'name':'marron','hex':'#8B4513'},
        {'id':5,'name':'bleu-ciel','hex':'#87ceeb'},
        {'id':6,'name':'beige','hex':'#f5f5dc'},
        {'id':7,'name':'argent','hex':'#c0c0c0'},
        {'id':8,'name':'or','hex':'#ffd700'},
        {'id':9,'name':'bleu','hex':'#000080'},
        {'id':10,'name':'rose','hex':'#ffc0cb'},
        {'id':11,'name':'violet','hex':'#800080'},
        {'id':12,'name':'rouge','hex':'#ff0000'},
    ]
    for color in liste:
        Color.objects.create(
            name = color['name'],
            value = color['hex']
        )


def populate_badge_table():
    liste = [
        {'id':1,'name':'Promotion','className':None},
        {'id':2,'name':'Collection','className':'light-blue'},
        {'id':3,'name':'Nouveau','className':'light-green'},
        {'id':4,'name':'Edition','className':'light-orange'},
    ]
    for badge in liste:
        Badge.objects.create(
            name = badge['name'],
            className = badge['className']
            )

def populate_tag_table():
    liste = [
        {'id':1,'name':'Cuir'},
        {'id':2,'name':'Rubber'},
        {'id':3,'name':'Textile'},
        {'id':4,'name':'Polyester'},
        {'id':5,'name':'EVA'},
        {'id':6,'name':'Mesh'},
        {'id':7,'name':'Coton'},
        {'id':8,'name':'Elasthanne'},
        {'id':9,'name':'Molletonné'},
        {'id':10,'name':'Nylon'},
        {'id':11,'name':'Spandex'},
        {'id':12,'name':'Soie'},
        {'id':13,'name':'Cristal'},
        {'id':14,'name':'Caoutchouc'},
        {'id':15,'name':'Laine'},
        {'id':16,'name':'Acier'},
    ]
    for tag in liste:
        Tag.objects.create(
            name = tag['name']
        )


def populate_product_table():
    try:
        listProduct = [
            {
                'title': 'Nike Air Force 1',
                'category': 'Sneakers',
                'colors': ['blanc', 'noir'],
                'sizes': ['36', '40', '41', '42', '43'],
                'tags': ['Cuir', 'Rubber', 'Textile'],
                'badge': None,
                'brand': 'Nike',
                'percent': None,
                'oldPrice': 120,
                'stock': 45,
                'warranty': None,
                'description': 'Chaussure iconique et intemporelle',
                'imgDefault':'images/sneaker.png',
                'imgHover':'images/sneaker-2.png',
            },
            {
                'title': 'T-Shirt Nike Sportswear',
                'category': 'T-shirt',
                'colors': ['blanc', 'noir'],
                'sizes': ['S', 'M', 'L', 'XL'],
                'tags': ['Coton', 'Polyester', 'Elasthanne'],
                'badge': 'Promotion',
                'brand': 'Nike',
                'percent': 25,
                'oldPrice': 45,
                'stock': 120,
                'warranty': None,
                'description': 'T-shirt confortable en coton',
                'imgDefault':'images/t-shirt.png',
                'imgHover':'images/t-shirt--1.png',
            },
            {
                'title': 'Chemise Adidas Essentials',
                'category': 'Chemise',
                'colors': ['noir'],
                'sizes': ['S', 'M', 'L', 'XL', 'XXL'],
                'tags': ['Coton', 'Soie', 'Polyester'],
                'badge': 'Collection',
                'brand': 'Adidas',
                'percent': 18,
                'oldPrice': 65,
                'stock': 70,
                'warranty': None,
                'description': 'Chemise élégante pour le quotidien',
                'imgDefault':'images/shirt.png',
                'imgHover':'images/shirt-1.png',
            },
            {
                'title': 'Costume  Executive',
                'category': 'Costume',
                'colors': ['noir', 'gris'],
                'sizes': ['S', 'M', 'L', 'XL'],
                'tags': ['Laine', 'Polyester', 'Soie'],
                'badge': 'Edition',
                'brand': 'Horizon',
                'percent': 22,
                'oldPrice': 380,
                'stock': 14,
                'warranty': None,
                'description': 'Costume executive haut de gamme',
                'imgDefault':'images/suit.png',
                'imgHover':'images/suit-1.png',
            },
            {
                'title': 'Montre Casio Chronographe',
                'category': 'Montre',
                'colors': ['noir', 'argent'],
                'sizes': None,
                'tags': ['Acier', 'Cristal', 'Caoutchouc'],
                'badge': 'Edition',
                'brand': 'Casio',
                'percent': None,
                'oldPrice': 250,
                'stock': 15,
                'warranty': 24,
                'description': 'Montre de sport précise et durable',
                'imgDefault':'images/watch.png',
                'imgHover':'images/watch-2.png'
            },
            {
            "title": "Adidas Ultraboost 22",
            "category": "Chaussure",
            "colors": ['noir','gris'],
            "sizes": ["36", "38", "39", "41", "42"],
            "badge": "Collection",
            "tags": ["Polyester", "EVA", "Textile"],
            "brand": "Adidas",
            "percent": 20,
            "oldPrice": 60,
            "stock": 75,
            "warranty": None,
            "description": "Bracelet en cuir véritable",
            'imgDefault':'images/shoes-11.png',
            'imgHover':'images/shoes-9.png',
        },
            {
                "title": "Costume Weston Full",    
                "category": "Costume",
                "colors": ['noir','gris'],
                "sizes": ["S", "M", "L", "XL"],
                "badge": "Promotion",
                'tags': ['Laine', 'Polyester', 'Soie'],
                "brand": "Horizon",
                "percent": 12,
                "oldPrice": 380,
                "stock": 14,
                "warranty": None,
                "description": "Costume executive haut de gamme",
                'imgDefault':'images/suit-4.png',
                'imgHover':'images/suit-5.png'
            },
            {
                "title": "Horizon Noir Premium",
                "category": "T-shirt",
                "colors": ['bleu'],
                "sizes": ["S", "M", "L", "XL"],
                "badge": "Collection",
                'tags': ['Laine', 'Polyester', 'Soie'],
                "brand": "Horizon",
                "percent": 15,
                "oldPrice": 420,
                "stock": 9,
                "warranty": None,
                "description": "Costume noir premium pour occasions spéciales",
                'imgDefault':'images/t-shirt-6.png',
                'imgHover':'images/t-shirt-6-1.png'
            },
            {
                "title": "Chemise Puma Formal White",
                "category": "Chemise",
                "colors": ['blanc'],
                "sizes": ["S", "M", "L", "XL"],
                "badge": "Nouveau",
                "tags": ["Soie", "Rubber", "Mesh"],
                "brand": "Puma",
                "percent": 10,
                "oldPrice": 70,
                "stock": 65,
                "warranty": None,
                "description": "Chemise formelle blanche élégante",
                'imgDefault':'images/product-1-1.jpg',
                'imgHover':'images/product-1-2.jpg'
            },
            {
                "title": "Chemise Nike Oxford",
                "category": "Chemise",
                "colors": ['bleu','beige'],
                "sizes": ["S", "M", "L", "XL"],
                "badge": "Collection",
                "tags": ["Coton", "Spandex", "Caoutchouc"],
                "brand": "Nike",
                "percent": 24,
                "oldPrice": 80,
                "stock": 50,
                "warranty": None,
                "description": "Chemise Oxford classique et intemporelle",
                'imgDefault':'images/shirt-2.png',
                'imgHover':'images/shirt-3.png'
            },
            {
                "title": "Puma RS-X",
                "category": "Chaussure",
                "colors": ['noir','marron'],
                "sizes": ["36", "38", "39", "41", "42"],
                "badge": "Nouveau",
                "tags": ["Textile", "Laine", "Mesh"],
                "brand": "Puma",
                "percent": 10,
                "oldPrice": 100,
                "stock": 28,
                "warranty": None,
                "description": "Design rétro futuriste",
                'imgDefault':'images/shoes-8.png',
                'imgHover':'images/shoes-3.png'
            },
            {
                "title": "Pull Adidas Essentials",
                "category": "Pull",
                "colors": ['gris','noir'],
                "sizes": ["S", "M", "L", "XL"],
                "badge": "Collection",
                "tags": ["Coton", "Polyester", "Molletonné"],
                "brand": "Adidas",
                "percent": 15,
                "oldPrice": 70,
                "stock": 85,
                "warranty": None,
                "description": "Sweat-shirt casual pour tous les jours",
                'imgDefault':'images/pull-2.png',
                'imgHover':'images/pull-1.png'
            }, 
            {
                "title": "Sac Ludic",
                "category": "Sac",
                "colors": ['gris','noir'],
                "sizes": None,
                "badge": "Collection",
                "brand": "Lacost",
                "tags": ["Cuir", "Textile", "Nylon"],
                "percent": 18,
                "oldPrice": 90,
                "stock": 40,
                "warranty": None,
                "description": "Sac à dos spacieux avec compartiments",
                'imgDefault':'images/bag-4.png',
                'imgHover':'images/bag-2.png',   
            },
            {
                "title": "Running Shorts Nike Flex",
                "category": "Short",
                "colors": ['noir','gris'],
                "sizes": ["XS", "S", "M", "L"],
                "badge": None,
                "tags": ["Coton", "Elasthanne", "Spandex"],
                "brand": "Nike",
                "percent": 22,
                "oldPrice": 60,
                "stock": 55,
                "warranty": None,
                "description": "Short léger et respirant pour la course",
                'imgDefault':'images/short-2.png',
                'imgHover':'images/short-3.png'
            },
            {
                "title": "T-shirt Adidas Essentials",
                "category": "T-shirt",
                "colors": ['blanc','noir'],
                "sizes": ["S", "M", "L", "XL", "XXL"],
                "badge": "Collection",
                "tags": ["Coton", "Elasthanne", "Spandex"],
                "brand": "Adidas",
                "percent": 18,
                "oldPrice": 65,
                "stock": 70,
                "warranty": None,
                "description": "Chemise élégante pour le quotidien",
                'imgDefault':'images/shirt-9.png',
                'imgHover':'images/t-shirt-5.png',
            },
            {
                "title": "Veste Puma Essentials",
                "category": "Pull",
                "colors": ['gris','noir','rouge'],
                "sizes": ["S", "M", "L", "XL"],
                "badge": "Nouveau",
                "brand": "Puma",
                "tags": ["Coton", "Elasthanne", "Spandex"],
                "percent": 25,
                "oldPrice": 110,
                "stock": 42,
                "warranty": None,
                "description": "Veste légère et élégante",
                'imgDefault':'images/sweater.png',
                'imgHover':'images/sweater-1.png',
            },
            {
                "title": "Ceinture Nike Reversible",
                "category": "Accessoire",
                "colors": ['noir','marron'],
                "sizes": None,
                "badge": "Promotion",
                "tags": ["Coton", "Textile", "Nylon"],
                "brand": "Luna",
                "percent": 35,
                "oldPrice": 40,
                "stock": 80,
                "warranty": None,
                "description": "Ceinture réversible deux en un",
                'imgDefault':'images/ceinture-1.png',
                'imgHover':'images/ceinture.png',
            },
            {
                "title": "Sandale Tiffany",
                "category": "Accessoire",
                "colors": ['bleu','or'],
                "sizes": None,
                "badge": "Collection",
                "tags": ["Polyester", "Nylon", "Molletonné"],
                "brand": "Adidas",
                "percent": 20,
                "oldPrice": 45,
                "stock": 95,
                "warranty": None,
                "description": "Bonnet chaud pour l'hiver",
                'imgDefault':'images/sandale.png',
                'imgHover':'images/sandale-1.png',
            },
            {
                "title": "Nike Workers",
                "category": "T-shirt",
                "colors": ['gris','noir'],
                "sizes": ["XS", "S", "M", "L", "XL"],
                "badge": None,
                "tags": ["Rubber", "EVA", "Mesh"],
                "brand": "Nike",
                "percent": 23,
                "oldPrice": 40,
                "stock": 130,
                "warranty": None,
                "description": "Débardeur respirant pour l'entraînement",
                'imgDefault':'images/t-shirt-2.png',
                'imgHover':'images/t-shirt-2.png',
            },
            {
                "title": "All Star",
                "category": "Sneakers",
                "colors": ['noir','rouge','bleu'],
                "sizes": ["36", "37",  "39", "40", "42"],
                "badge": "Collection",
                "tags": ["Elasthanne", "Mesh", "Textile"],
                "brand": "Converse",
                "percent": 30,
                "oldPrice": 95,
                "stock": 55,
                "warranty": None,
                "description": "Chaussure de style vintage revisité",
                'imgDefault':'images/snearkes-1.png',
                'imgHover':'images/snearkes-2.png',
            }, 
            {
                "title": 'Platium lointine',
                "category": "Montre",
                "colors": None,
                "sizes": None,
                "badge": None,
                "tags": ["Molletonné", "Rubber", "Textile"],
                "brand": "Clementino",
                "percent": 15,
                "oldPrice": 390,
                "stock": 48,
                "warranty": 3,
                "description": "Montre classique en daim",
                'imgDefault':'images/watch-4.png',
                'imgHover':'images/watch-5.png',
            },
            {
                "title": "Nike Deland",
                "category": "Short",
                "colors": ['gris','noir'],
                "sizes": ['S','M','L'],
                "badge": None,
                "tags": ["Nylon", "Spandex", "Polyester"],
                "brand": "Noke",
                "percent": 18,
                "oldPrice": 40,
                "stock": 32,
                "warranty": None,
                "description": "Chaussure de basket haute performance",
                'imgDefault':'images/short-5.png',
                'imgHover':'images/short-4.png',
            },
            {
                "title": "Pull Flamer display",
                "category": "Pull",
                "colors": ['gris','noir'],
                "sizes": ['S','M','L','XL'],
                "badge": None,
                "tags": ["Coton", "Mesh", "Textile"],
                "brand": "Flamer",
                "percent": 22,
                "oldPrice": 160,
                "stock": 28,
                "warranty": None,
                "description": "Chaussure de trail robuste et légère",
                'imgDefault':'images/pull-4.png',
                'imgHover':'images/pull-3.png',
            },
            {
                "title": "Baskets Adidas ZX",
                "category": "Sneakers",
                "colors": ['blanc','noir'],
                "sizes": ["36", "37", "38", "39", "40", "43"],
                "badge": "Nouveau",
                "tags": ["Rubber", "Elasthanne", "Nylon"],
                "brand": "Adidas",
                "percent": 20,
                "oldPrice": 85,
                "stock": 58,
                "warranty": None,
                "description": "Baskets rétro avec style moderne",
                'imgDefault':'images/sneaker-4.png',
                'imgHover':'images/sneaker-5.png',
            },
            {
                "title": "Luivitton Sky bord",
                "category": "Sac",
                "colors": ['marron','noir'],
                "sizes": None,
                "badge": "Edition",
                "tags": ["Elasthanne", "Mesh", "Textile"],
                "brand": "Luivitton",
                "percent": 10,
                "oldPrice": 2980,
                "stock": 8,
                "warranty": 5,
                "description": "Sac Luivitton mécanique prestige",
                'imgDefault':'images/bac_lui.png',
                'imgHover':'images/bag-1.png',
            },
        ]
        for product_data in listProduct:
            category= Category.objects.get(name=product_data['category'])
            badge = None
            if product_data['badge']:
                badge = Badge.objects.get(name=product_data['badge'])

            product = Product.objects.create(
                title = product_data['title'],
                category = category,
                badge = badge,
                brand = product_data['brand'],
                percent = product_data['percent'],
                oldPrice = product_data['oldPrice'],
                stock = product_data['stock'],
                warranty = product_data['warranty'],
                description = product_data['description'],
                imgDefault = product_data['imgDefault'],
                imgHover = product_data['imgHover']
            )
       
            if product_data['colors']:
                for color_name in product_data['colors']:
                    color = Color.objects.get(name=color_name)
                    product.color.add(color)
        
            if product_data['sizes']:
                for size_code in product_data['sizes']:
                    size = Size.objects.get(code=size_code)
                    product.size.add(size)
        
            if product_data['tags']:
                print('liste : ',product_data['tags'])
                for tag_name in product_data['tags']:
                    print('element : ',tag_name)
                    tag = Tag.objects.get(name=tag_name)
                    product.tag.add(tag)
            print("Produit crée : ",product.title)
    except Exception as e:
        print(e)


if __name__=='__main__':
    
    print('Remplissage des catégories')
    populate_category_table()
    print('Remplissage des tailles')
    populate_size_table()
    print('Remplissage des couleurs')
    populate_color_table()
    print('Remplissage de badges')
    populate_badge_table()
    print('Remplissage de tags')
    populate_tag_table()
    print('Remplissage de produits')
    populate_product_table()
    print('Base de données remplie avec succès !')