import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arthur.settings')
import django
django.setup()
from api.models import Product,Category,Size,Color,Badge,Tag

from faker import Faker

faker = Faker()

list_category = [
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
list_color = [
    {'id':1,'name':'blanc','hex':'#F2F5F0'},
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
    {'id':13,'name':'vert','hex':'#0A663B'},
    {'id':14,'name':None,'hex':None}
]
list_badge = [
    {'id':1,'name':'Promotion','className':None},
    {'id':2,'name':'Collection','className':'light-blue'},
    {'id':3,'name':'Nouveau','className':'light-green'},
    {'id':4,'name':'Edition','className':'light-orange'},
    {'id':5,'name':None,'className':None}
]

list_tag = [
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
    {'id': 17, 'name': 'Saphir'},
    {'id': 18, 'name': 'Or'},
    {'id': 19, 'name': 'Monogram'},
]

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
                'imgHover':'images/t-shirt-3.png',
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
            {
                'title': 'Converse  Taylor All Star',
                'category': 'Sneakers',
                'colors': ['blanc', 'noir'],
                'sizes': ['36', '37', '40', '41', '42'],
                'tags': ['Textile', 'Rubber', 'Coton'],
                'badge': 'Collection',
                'brand': 'Converse',
                'percent': 20,
                'oldPrice': 65,
                'stock': 72,
                'warranty': None,
                'description': 'Baskets iconiques incontournables',
                'imgDefault':'images/sneaker-3.png',
                'imgHover': 'images/sneaker-6.png',
            },
            {
                'title': 'New Balance 574',
                'category': 'Sneakers',
                'colors': ['gris', 'noir', 'blanc'],
                'sizes': ['36', '37', '38', '41', '42'],
                'tags': ['Mesh', 'Rubber', 'EVA'],
                'badge': 'Nouveau',
                'brand': 'New Balance',
                'percent': 25,
                'oldPrice': 110,
                'stock': 58,
                'warranty': None,
                'description': 'Confort premium pour la marche',
                'imgDefault': 'images/sneakers-3.png',
                'imgHover': 'images/sneakers-4.png',
            },
            {
                'title': 'Vans Old Skool',
                'category': 'Sneakers',
                'colors': ['noir', 'blanc'],
                'sizes': ['37', '38', '40', '41', '42'],
                'tags': ['Textile', 'Rubber','Nylon'],
                'badge': 'Promotion',
                'brand': 'Vans',
                'percent': 22,
                'oldPrice': 75,
                'stock': 65,
                'warranty': None,
                'description': 'Classique du skateboard',
                'imgDefault': 'images/sneaker-9.png',
                'imgHover': 'images/sneaker-10.png',
            },
            {
                'title': 'T-Shirt Lacoste Basic',
                'category': 'T-shirt',
                'colors': ['blanc', 'noir'],
                'sizes': ['XS', 'S', 'M', 'L', 'XL'],
                'tags': ['Coton', 'Elasthanne', 'Textile'],
                'badge': 'Collection',
                'brand': 'Lacoste',
                'percent': 30,
                'oldPrice': 55,
                'stock': 95,
                'warranty': None,
                'description': 'T-shirt elegant et minimaliste',
                'imgDefault': 'images/t-shirt-7.png',
                'imgHover': 'images/t-shirt-8.png',
            },
            {
                'title': 'T-Shirt Tommy Hilfiger',
                'category': 'T-shirt',
                'colors': ['blanc', 'rouge'],
                'sizes': ['S', 'M', 'L', 'XL', 'XXL'],
                'tags': ['Coton', 'Polyester', 'Elasthanne'],
                'badge': 'Nouveau',
                'brand': 'Tommy Hilfiger',
                'percent': 20,
                'oldPrice': 50,
                'stock': 88,
                'warranty': None,
                'description': 'T-shirt premium avec logo',
                'imgDefault': 'images/t-shirt-9.png',
                'imgHover': 'images/t-shirt-10.png',
            },
            {
                'title': 'T-Shirt Calvin Klein',
                'ref': 'CAL001',
                'category': 'T-shirt',
                'colors': ['noir', 'blanc', 'gris'],
                'sizes': ['XS', 'S', 'M', 'L', 'XL'],
                'tags': ['Coton', 'Elasthanne', 'Textile'],
                'badge': None,
                'brand': 'Calvin Klein',
                'percent': 25,
                'oldPrice': 60,
                'stock': 110,
                'warranty': None,
                'description': 'T-shirt minimaliste de luxe',
                'imgDefault': 'images/t-shirt-11.png',
                'imgHover': 'images/t-shirt-8.png',
            },
            {
                'title': 'Asics Gel-Lyte III',
                'category': 'Chaussure',
                'colors': ['gris', 'noir'],
                'sizes': ['36', '37', '38', '40', '42'],
                'tags': ['Rubber', 'Mesh', 'Cuir'],
                'badge': 'Edition',
                'brand': 'Asics',
                'percent': None,
                'oldPrice': 130,
                'stock': 42,
                'warranty': None,
                'description': 'Chaussure rétro iconique',
                'imgDefault': 'images/shoe-5.png',
                'imgHover': 'images/shoe-7.png',
            },
            {
                'title': 'Reebok Classic Leather',
                'category': 'Chaussure',
                'colors': ['blanc', 'noir'],
                'sizes': ['36',  '38', '40', '41', '42'],
                'tags': ['Cuir', 'Rubber', 'Textile'],
                'badge': 'Promotion',
                'brand': 'Reebok',
                'percent': 35,
                'oldPrice': 85,
                'stock': 54,
                'warranty': 2,
                'description': 'Chaussure classique intemporelle',
                'imgDefault': 'images/shoes-10.png',
                'imgHover': 'images/shoes-9.png',
            },
            {
                'title': 'Manteau Mango Wool',
                'category': 'Manteaux',
                'colors': ['marron', 'noir', 'gris'],
                'sizes': ['S', 'M', 'L', 'XL'],
                'tags': ['Laine', 'Polyester', 'Nylon'],
                'badge': 'Nouveau',
                'brand': 'Mango',
                'percent': 20,
                'oldPrice': 160,
                'stock': 38,
                'warranty': None,
                'description': 'Manteau élégant en laine',
                'imgDefault': 'images/coat-5.png',
                'imgHover': 'images/coat-5.png',
            },
            {
                'title': 'Manteau Zara Minimalist',
                'category': 'Manteaux',
                'colors': ['noir', 'beige'],
                'sizes': ['XS', 'S', 'M', 'L', 'XL'],
                'tags': ['Polyester', 'Nylon', 'Laine'],
                'badge': None,
                'brand': 'Zara',
                'percent': 25,
                'oldPrice': 140,
                'stock': 45,
                'warranty': None,
                'description': 'Manteau épuré et moderne',
                'imgDefault': 'images/coat-8.png',
                'imgHover': 'images/coat-7.png',
            },
            {
                'title': 'Chemise Ralph Lauren Oxford',
                'category': 'Chemise',
                'colors': ['bleu'],
                'sizes': ['S', 'M', 'L', 'XL', 'XXL'],
                'tags': ['Coton', 'Polyester', 'Soie'],
                'badge': 'Edition',
                'brand': 'Ralph Lauren',
                'percent': 10,
                'oldPrice': 95,
                'stock': 62,
                'warranty': None,
                'description': 'Chemise oxford premium',
                'imgDefault': 'images/shirt-5.png',
                'imgHover': 'images/shirt-4.png',
            },
            {
                'title': 'Chemise Burberry Nova Check',
                'category': 'Chemise',
                'colors': ['rouge', 'noir'],
                'sizes': ['S', 'M', 'L', 'XL'],
                'tags': ['Coton', 'Soie', 'Elasthanne'],
                'badge': 'Nouveau',
                'brand': 'Burberry',
                'percent': 8,
                'oldPrice': 180,
                'stock': 28,
                'warranty': None,
                'description': 'Chemise luxe avec motif signature',
                'imgDefault': 'images/shirt-7.png',
                'imgHover': 'images/shirt-6.png',
            },
            {
                'title': 'Pull Gucci Wool',
                'category': 'Pull',
                'colors': ['noir', 'beige'],
                'sizes': ['XS', 'S', 'M', 'L', 'XL'],
                'tags': ['Laine', 'Soie', 'Coton'],
                'badge': 'Edition',
                'brand': 'Gucci',
                'percent': None,
                'oldPrice': 250,
                'stock': 18,
                'warranty': None,
                'description': 'Pull de luxe en laine fine',
                'imgDefault': 'images/pull-5.png',
                'imgHover': 'images/pull-6.png',
            },

            {
                'title': 'Pull Stella McCartney',
                'category': 'Pull',
                'colors': ['gris', 'noir'],
                'sizes': ['S', 'M', 'L', 'XL', 'XXL'],
                'tags': ['Laine', 'Coton', 'Elasthanne'],
                'badge': 'Promotion',
                'brand': 'Stella McCartney',
                'percent': 22,
                'oldPrice': 180,
                'stock': 35,
                'warranty': None,
                'description': 'Pull luxe et durable',
                'imgDefault': 'images/pull-5.png',
                'imgHover': 'images/pull-6.png',
            },
            {
                'title': 'Short Adidas Climalite',
                'category': 'Short',
                'colors': ['noir', 'blanc'],
                'sizes': ['XS', 'S', 'M', 'L', 'XL'],
                'tags': ['Polyester', 'Elasthanne', 'Mesh'],
                'badge': 'Collection',
                'brand': 'Adidas',
                'percent': 40,
                'oldPrice': 60,
                'stock': 70,
                'warranty': None,
                'description': 'Short de sport respirant',
                'imgDefault': 'images/short-7.png',
                'imgHover': 'images/short-6.png',
            },
            {
                'title': 'Sac Gucci Marmont',
                'category': 'Sac',
                'colors': ['noir', 'rouge'],
                'sizes': None,
                'tags': ['Cuir', 'Textile', 'Caoutchouc'],
                'badge': 'Edition',
                'brand': 'Gucci',
                'percent': 30,
                'oldPrice': 450,
                'stock': 8,
                'warranty': 2,
                'description': 'Sac à main de luxe',
                'imgDefault': 'images/bag.png',
                'imgHover': 'images/bag-3.png',
            },
            {
                'title': 'Sac Louis Vuitton Neverfull',
                'category': 'Sac',
                'colors': ['marron', 'noir'],
                'sizes': None,
                'tags': ['Cuir', 'Textile', 'Monogram'],
                'badge': 'Nouveau',
                'brand': 'Louis Vuitton',
                'percent': None,
                'oldPrice': 1200,
                'stock': 3,
                'warranty': None,
                'description': 'Sac tote iconic de luxe',
                'imgDefault': 'images/bag-8.png',
                'imgHover': 'images/bag-9.png',
            },
            {
                'title': 'Hermes Silk Scarf',
                'category': 'Accessoire',
                'colors': ['rouge'],
                'sizes': None,
                'tags': ['Soie', 'Textile', 'Caoutchouc'],
                'badge': 'Edition',
                'brand': 'Hermès',
                'percent': None,
                'oldPrice': 100,
                'stock': 12,
                'warranty': None,
                'description': 'Foulard en soie de prestige',
                'imgDefault': 'images/scarf.png',
                'imgHover': 'images/scarf-1.png',
            },
            {
                'title': 'Costume Versace Silk',
                'category': 'Costume',
                'colors': ['noir','bleu'],
                'sizes': ['S', 'M', 'L', 'XL'],
                'tags': ['Soie', 'Laine', 'Polyester'],
                'badge': 'Edition',
                'brand': 'Versace',
                'percent': 15,
                'oldPrice': 1500,
                'stock': 5,
                'warranty': None,
                'description': 'Costume de prestige en soie',
                'imgDefault': 'images/coat.png',
                'imgHover': 'images/coat-2.png',
            },
            {
                'title': 'Montre Rolex Datejust',
                'category': 'Montre',
                'colors': ['argent', 'or'],
                'sizes': None,
                'tags': ['Acier', 'Or', 'Cristal', 'Saphir'],
                'badge': 'Edition',
                'brand': 'Rolex',
                'percent': None,
                'oldPrice': 5500,
                'stock': 2,
                'warranty': 60,
                'description': 'Montre de prestige légendaire',
                'imgDefault': 'images/watch-3.png',
                'imgHover': 'images/watch-4.png',
            }
        ]
list_size = [
    None,'XS','S','M','L','XL','XXL','36','37','38','39','40','41','42','43','44','45'
]
list_imageHover = []
list_imageDefault = []

for image in listProduct:
    list_imageHover.append(image['imgHover'])
    list_imageDefault.append(image['imgDefault'])

def populate_category_table():
    for item in list_category:
        Category.objects.create(
            name = item['name'],
            thumbnail = item['image']
        )

def populate_size_table():    
    for size in list_size:
        if size:
            Size.objects.create(
                code = size
            )

def populate_color_table():
    for color in list_color:
        if color['name']:
            Color.objects.create(
                name = color['name'],
                value = color['hex']
            )


def populate_badge_table():
    for badge in list_badge:
        if badge['name']:
            Badge.objects.create(
                name = badge['name'],
                className = badge['className']
                )

def populate_tag_table():
    for tag in list_tag:
        if tag['name']:
            Tag.objects.create(
                name = tag['name']
            )


def populate_product_table():
    try:      
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

def populate_personal_product(nbre):
    for _ in range(nbre):
        category = Category.objects.get(name = random.choice(list_category)['name'])
        badge = random.choice(list_badge)
        badgeValue = None
        if badge['name']:
            badgeValue = Badge.objects.get(name=badge['name'])
       
        product = Product.objects.create(
            title= faker.sentence(nb_words=3).replace('.', ''),
            category=category,
            badge = badgeValue,
            brand=faker.company(),
            percent = random.choice([None,15,20,25,30,40,45,50]),
            stock = random.randint(5,50),
            oldPrice = random.randint(50,2500),
            warranty = random.randint(1,3),
            description = faker.text(max_nb_chars=200),
            imgDefault = random.choice(list_imageDefault),
            imgHover = random.choice(list_imageHover)
        )
        colors = random.sample([c for c in list_color if c['name']], k=min(3, len([c for c in list_color if c['name']])))
        colorValue = None
        for color in colors:
            if color['name']:
                colorValue = Color.objects.get(name=color['name'])
                product.color.add(colorValue)
        
        sizes = random.choices(list_size,k=4)
        sizeValue = None
        for size in sizes:
            if size:
                sizeValue = Size.objects.get(code=size)
                product.size.add(sizeValue)
        tags = random.choices(list_tag,k=3)
        tagValue = None
        for tag in tags:
            if tag['name']:
                tagValue = Tag.objects.get(name=tag['name'])
                product.tag.add(tagValue)
        print("Produit crée : ",product.title)
        
if __name__=='__main__':
    nbre = int(input('Entrer le nombre de produit \t'))
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
    populate_personal_product(nbre)   