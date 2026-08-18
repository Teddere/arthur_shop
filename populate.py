import os
import random
from itertools import product

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arthur.settings')
import django
django.setup()
from api.models import Product,ProductItem,Category,Size,Color,Badge,Tag

from faker import Faker

faker = Faker()

list_category = [
    {'id':1,'name':'Sneakers','image':'images/snearkes.png'},
    {'id':2,'name':'T-shirt','image':'images/t-shirt.png'},
    {'id':3,'name':'Chaussure','image':'images/shoes-11.png'},
    {'id':4,'name':'Manteaux','image':'images/coat-9.png'},
    {'id':5,'name':'Chemise','image':'images/shirt-5.png'},
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
    {'id':5,'name':'ciel','hex':'#87ceeb'},
    {'id':6,'name':'beige','hex':'#f5f5dc'},
    {'id':7,'name':'argent','hex':'#c0c0c0'},
    {'id':8,'name':'or','hex':'#ffd700'},
    {'id':9,'name':'bleu','hex':'#000080'},
    {'id':10,'name':'rose','hex':'#ffc0cb'},
    {'id':11,'name':'violet','hex':'#800080'},
    {'id':12,'name':'rouge','hex':'#ff0000'},
    {'id':13,'name':'vert','hex':'#0A663B'},
    {'id':14,'name':'unique','hex':None}
]
list_badge = [
    {'id':1,'name':'Promotion','className':None},
    {'id':2,'name':'Collection','className':'light-blue'},
    {'id':3,'name':'Nouveau','className':'light-green'},
    {'id':4,'name':'Edition','className':'light-orange'},
#    {'id':5,'name':None,'className':None}
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
list_size = [
    'unique', 'XS', 'S', 'M', 'L', 'XL', 'XXL', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45'
]
listProducts = [
    {
        'title': 'Nike Air Force 1',
        'category': 'Sneakers',
        'colors': ['blanc', 'noir'],
        'sizes': [
            {'36': [
                {'color':'blanc','oldPrice':None,'percent':None,'stock': random.randint(0,30)},
                {'color':'noir','price':None,'percent':None,'stock': random.randint(0,30)}
            ]},
            {'40' : [
                {'color':'blanc','oldPrice':None,'percent':None,'stock': random.randint(0,30)},
                {'color':'noir','price':None,'percent':None,'stock': random.randint(0,30)}
            ]},
            {'41' : [
                {'color':'blanc','oldPrice':None,'percent':None,'stock': random.randint(0,30)},
                {'color':'noir','price':None,'percent':None,'stock': random.randint(0,30)}
            ]},
            {'42' : [
                {'color':'blanc','oldPrice':None,'percent':None,'stock': random.randint(0,30)},
                {'color':'noir','price':None,'percent':None,'stock': random.randint(0,30)}
            ]},
            {'43' : [
                {'color':'blanc','oldPrice':None,'percent':None,'stock': random.randint(0,30)},
                {'color':'noir','price':None,'percent':None,'stock': random.randint(0,30)}
            ]},
        ],
        'tags': ['Cuir', 'Caoutchouc', 'Textile', 'Semelle coussinée'],
        'badge': None,
        'brand': 'Nike',
        'price': 120,
        'warranty': None,
        'imgDefault': 'images/sneaker.png',
        'imgHover': 'images/sneaker-2.png',
        'description': "La Nike Air Force 1 est une sneaker iconique qui a marqué l'histoire du streetwear. Son cuir blanc immaculé offre un look épuré, tandis que sa semelle épaisse en caoutchouc garantit un confort optimal au quotidien. Idéale pour un usage urbain, elle se pare d'une tige en textile respirant et d'une semelle intérieure coussinée pour absorber les chocs. Cette version intemporelle reste un incontournable.",
    },
    {
        'title': 'T-Shirt Nike Sportswear',
        'category': 'T-shirt',
        'colors': ['blanc', 'noir'],
        'sizes': [
            {
                'S' : [
                    {'color':'blanc','oldPrice':None,'percent':25,'stock': random.randint(0,10)},
                    {'color':'noir','oldPrice':None,'percent':25,'stock': random.randint(0,15)},
                ]
            },
            {
                'M' : [
                    {'color':'blanc','oldPrice': 50,'percent':25,'stock': random.randint(0,10)},
                    {'color':'noir','oldPrice': 50,'percent':25,'stock': random.randint(0,15)},
                ]
            },
            {
                'L' : [
                    {'color':'blanc','oldPrice': 55,'percent':25,'stock': random.randint(0,10)},
                    {'color':'noir','oldPrice': 55,'percent':25,'stock': random.randint(0,15)},
                ]
            },
            {
                'XL' : [
                    {'color':'blanc','oldPrice': 60,'percent':25,'stock': random.randint(0,10)},
                    {'color':'noir','oldPrice': 60,'percent':25,'stock': random.randint(0,5)},
                ]
            },
        ],
        'tags': ['Coton', 'Polyester', 'Elasthanne', 'Coupe athlétique'],
        'badge': 'Promotion',
        'brand': 'Nike',
        'percent': 25,
        'price': 45,
        'stock': 120,
        'warranty': None,
        'imgDefault': 'images/t-shirt.png',
        'imgHover': 'images/t-shirt--1.png',
        'description': "Ce t-shirt Nike Sportswear allie simplicité et performance. Confectionné à partir d'un mélange de coton doux et de polyester respirant, il évacue l'humidité efficacement. L'ajout d'élasthanne lui confère une légère élasticité pour une liberté de mouvement totale. Sa coupe athlétique épouse le corps sans serrer, ce qui en fait le compagnon idéal pour vos entraînements ou vos journées décontractées. Une valeur sûre.",
    },
    {
        'title': 'Chemise Adidas Essentials',
        'category': 'Chemise',
        'colors': ['noir','marron'],
        'sizes': [
            {
                'S': [
                    {'color': 'noir', 'oldPrice': None, 'percent': 18, 'stock': random.randint(0, 10)},
                    {'color': 'marron', 'oldPrice': None, 'percent': 18, 'stock': random.randint(0, 10)},
                ]
            },
            {
                'M':[
                    {'color': 'noir', 'oldPrice': 70, 'percent': 18, 'stock': random.randint(0, 10)},
                    {'color': 'marron', 'oldPrice': 70, 'percent': 18, 'stock': random.randint(0, 10)},
                ]
            },
            {
                'L':[
                    {'color': 'noir', 'oldPrice': 75, 'percent': 18, 'stock': random.randint(0, 10)},
                ]
            },
            {
                'XL':[
                    {'color': 'noir', 'oldPrice': 80, 'percent': 18, 'stock': random.randint(0, 10)},
                ]
            },
            {
                'XXL':[
                    {'color': 'noir', 'oldPrice': 90, 'percent': 18, 'stock': random.randint(0, 5)},
                ]
            },
        ],
        'tags': ['Coton', 'Soie', 'Polyester'],
        'badge': 'Collection',
        'brand': 'Adidas',
        'percent': 18,
        'price': 65,
        'stock': 70,
        'warranty': None,
        'imgDefault': 'images/shirt.png',
        'imgHover': 'images/shirt-1.png',
        'description': "La chemise Adidas Essentials se distingue par son style épuré et sa coupe confortable. Confectionnée en coton doux mélangé à du polyester pour une meilleure tenue, elle intègre un peu d'élasthanne afin de suivre vos mouvements. Son col classique apporte une touche d'élégance décontractée, parfaite pour le bureau ou les sorties entre amis. Facile à repasser et résistante, cette chemise noire deviendra vite un basique de votre dressing.",
    },
    {
        'title': 'Costume  Executive',
        'category': 'Costume',
        'colors': ['noir', 'gris'],
        'sizes': [
            {
                'S': [
                    {'color': 'noir', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 20)},
                    {'color': 'gris', 'oldPrice': None, 'percent': 18, 'stock': random.randint(0, 3)},
                ]
            },
            {
                'M': [
                    {'color': 'noir', 'oldPrice': 390, 'percent': 22, 'stock': random.randint(0, 20)},
                    {'color': 'gris', 'oldPrice': 390, 'percent': 18, 'stock': random.randint(0, 9)},
                ]
            },
            {
                'L': [
                    {'color': 'gris', 'oldPrice': 400, 'percent': 18, 'stock': random.randint(0, 10)},
                ]
            },
            {
                'XL': [
                    {'color': 'gris', 'oldPrice': 400, 'percent': 30, 'stock': random.randint(0, 5)},
                ]
            },
        ],
        'tags': ['Laine', 'Polyester', 'Soie'],
        'badge': 'Edition',
        'brand': 'Horizon',
        'percent': 22,
        'price': 380,
        'stock': 14,
        'warranty': None,
        'imgDefault': 'images/suit.png',
        'imgHover': 'images/suit-1.png',
        'description': "Le costume Executive d'Horizon est taillé pour les professionnels exigeants. Composé de laine noble, de polyester anti-froisse et de viscose fluide, il offre une excellente respirabilité et un tombé parfait. Sa coupe ajustée souligne la silhouette sans contraindre, avec des épaules structurées et une longueur de veste moderne. Livré avec un pantalon plat, il convient aux mariages, réunions importantes ou soirées chic. Un investissement durable.",
    },
    {
        'title': 'Montre Casio Chronographe',
        'category': 'Montre',
        'colors': ['noir', 'argent'],
        'sizes': [
            {
                'unique': [
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                    {'color': 'argent', 'oldPrice': 300, 'percent': None, 'stock': random.randint(0, 20)},
                ]
            },
        ],
        'tags': ['Acier', 'Cristal', 'Caoutchouc'],
        'badge': 'Edition',
        'brand': 'Casio',
        'percent': None,
        'price': 250,
        'stock': 15,
        'warranty': 24,
        'imgDefault': 'images/watch.png',
        'imgHover': 'images/watch-2.png',
        'description': "La montre Casio Chronographe allie robustesse et précision. Son boîtier en acier inoxydable résiste aux chocs, tandis que son verre minéral protège le cadran des rayures. Le bracelet en caoutchouc souple assure un maintien confortable même lors d'activités sportives. La fonction chronomètre vous permet de mesurer des temps intermédiaires avec exactitude. Idéale pour les athlètes ou les amateurs de montres fonctionnelles, elle affiche une autonomie de batterie prolongée",
    },
    {
        "title": "Adidas Ultraboost 22",
        "category": "Chaussure",
        "colors": ['noir', 'gris'],
        "sizes": [
            {
                '36': [
                    {'color': 'noir', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 20)},
                    {'color': 'gris', 'oldPrice': 70, 'percent': 22, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '38': [
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                    {'color': 'gris', 'oldPrice': 70, 'percent': None, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '39': [
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                    {'color': 'gris', 'oldPrice': 70, 'percent': None, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '41': [
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                    {'color': 'gris', 'oldPrice': 70, 'percent': None, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '42': [
                    {'color': 'gris', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                ]
            },
        ],
        "badge": "Collection",
        "tags": ["Polyester", "EVA", "Textile"],
        "brand": "Adidas",
        "percent": 20,
        "price": 60,
        "stock": 75,
        "warranty": None,
        'imgDefault': 'images/shoes-11.png',
        'imgHover': 'images/shoes-9.png',
        "description": "L'Adidas Ultraboost 22 est une chaussure de running haute performance. Sa tige en textile Primeknit+ épouse parfaitement le pied pour un maintien sans couture. La semelle intermédiaire en EVA offre un amorti dynamique à chaque foulée, tandis que le caoutchouc Continental garantit une adhérence exceptionnelle sur sol sec et humide. Idéal pour les longues distances, ce modèle noir et gris conjugue légèreté et réactivité. Un must pour les coureurs exigeants.",
    },
    {
        "title": "Costume Weston Full",
        "category": "Costume",
        "colors": ['noir', 'gris'],
        "sizes": [
            {
                'S': [
                    {'color': 'noir', 'oldPrice': None, 'percent': 12, 'stock': random.randint(0, 20)},
                    {'color': 'gris', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'M': [
                    {'color': 'noir', 'oldPrice': 400, 'percent': 12, 'stock': random.randint(0, 20)},
                    {'color': 'gris', 'oldPrice': 400, 'percent': 10, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'L': [
                    {'color': 'noir', 'oldPrice': 450, 'percent': 15, 'stock': random.randint(0, 20)},
                    {'color': 'gris', 'oldPrice': 450, 'percent': 20, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'XL': [
                    {'color': 'noir', 'oldPrice': 480, 'percent': 10, 'stock': random.randint(0, 20)},
                    {'color': 'gris', 'oldPrice': 480, 'percent': 25, 'stock': random.randint(0, 20)},
                ]
            },
        ],
        "badge": "Promotion",
        'tags': ['Laine', 'Polyester', 'Soie'],
        "brand": "Horizon",
        "percent": 12,
        "price": 380,
        "warranty": None,
        'imgDefault': 'images/suit-4.png',
        'imgHover': 'images/suit-5.png',
        "description": "Le costume Weston Full se distingue par son double boutonnage élégant et sa coupe moderne. Taillé dans un mélange de laine, polyester et viscose, il résiste aux froissements et conserve sa forme toute la journée. La veste propose des poches intérieures pratiques, et le pantalon à plis offre une liberté de mouvement accrue. Parfait pour les cérémonies ou les rendez-vous d'affaires, ce costume gris/noir dégage une assurance naturelle. Une promotion à saisir.",
    },
    {
        "title": "Horizon Noir Premium",
        "category": "T-shirt",
        "colors": ['bleu'],
        "sizes": [
            {
                'S' : [
                    {'color': 'bleu', 'oldPrice': None, 'percent': 15, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'M' : [
                    {'color': 'bleu', 'oldPrice': 440, 'percent': 15, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'L' : [
                    {'color': 'bleu', 'oldPrice': 460, 'percent': 15, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'XL' : [
                    {'color': 'bleu', 'oldPrice': 480, 'percent': 15, 'stock': random.randint(0, 20)},
                ]
            },
        ],
        "badge": "Collection",
        'tags': ['Laine', 'Polyester', 'Soie'],
        "brand": "Horizon",
        "percent": 15,
        "price": 420,
        "stock": 9,
        "warranty": None,
        'imgDefault': 'images/t-shirt-6.png',
        'imgHover': 'images/t-shirt-6-1.png',
        "description": "Le t-shirt Horizon Noir Premium est bien plus qu'un simple haut : c'est une déclaration de style. Bien que sa description originale parle d'un costume, ce t-shirt bleu en coton, polyester et élasthanne offre une extensibilité exceptionnelle. Son col V met en valeur la poitrine, et sa coupe ajustée souligne les épaules. Parfait pour les soirées ou les rendez-vous, il se marie aussi bien avec un jean qu'avec un blazer. Une pièce de collection.",
    },
    {
        "title": "Chemise Puma Formal White",
        "category": "Chemise",
        "colors": ['blanc'],
        "sizes": [
            {
                'S': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 15, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'M': [
                    {'color': 'blanc', 'oldPrice': 75, 'percent': 15, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'L': [
                    {'color': 'blanc', 'oldPrice': 80, 'percent': 15, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'XL': [
                    {'color': 'blanc', 'oldPrice': 85, 'percent': 15, 'stock': random.randint(0, 20)},
                ]
            },
            ],
        "badge": "Nouveau",
        "tags": ["Soie", "Rubber", "Mesh"],
        "brand": "Puma",
        "percent": 10,
        "price": 70,
        "stock": 65,
        "warranty": None,
        'imgDefault': 'images/product-1-1.jpg',
        'imgHover': 'images/product-1-2.jpg',
        "description": "La chemise Puma Formal White est taillée pour les hommes d'affaires modernes. Confectionnée à partir de coton peigné doux, de polyester résistant et d'élasthanne pour une aisance de mouvement, elle arbore des boutons nacrés qui ajoutent une touche de luxe discret. Sa coupe formelle reste confortable, sans excès de matière. Blanche immaculée, elle se porte aussi bien avec un costume sombre qu'avec un pantalon chino. Un indispensable de la garde-robe professionnelle.",
    },
    {
        "title": "Chemise Nike Oxford",
        "category": "Chemise",
        "colors": ['bleu', 'beige'],
        "sizes": [
            {
                'S': [
                    {'color': 'bleu', 'oldPrice': None, 'percent': 15, 'stock': random.randint(0, 20)},
                    {'color': 'beige', 'oldPrice': None, 'percent': 15, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'M': [
                    {'color': 'bleu', 'oldPrice': 85, 'percent': 15, 'stock': random.randint(0, 20)},
                    {'color': 'beige', 'oldPrice': 85, 'percent': 15, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'L': [
                    {'color': 'bleu', 'oldPrice': 90, 'percent': 15, 'stock': random.randint(0, 20)},
                    {'color': 'beige', 'oldPrice': 95, 'percent': 15, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'XL': [
                    {'color': 'bleu', 'oldPrice': 90, 'percent': None, 'stock': random.randint(0, 20)},
                ]
            },
        ],
        "badge": "Collection",
        "tags": ["Coton", "Spandex", "Caoutchouc"],
        "brand": "Nike",
        "percent": 24,
        "price": 80,
        "stock": 50,
        "warranty": None,
        'imgDefault': 'images/shirt-2.png',
        'imgHover': 'images/shirt-3.png',
        "description": "La chemise Nike Oxford revisite un classique du vestiaire masculin. En coton Oxford texturé mélangé à du polyester et un peu d'élasthanne, elle offre une tenue parfaite sans se froisser facilement. Sa poche poitrine discrète permet de ranger un petit accessoire. Les coloris bleu et beige se marient avec la plupart des pantalons. Que ce soit pour le bureau ou un dîner, cette chemise dégage un charme intemporel et une allure soignée. Une valeur sûre.",
    },
    {
        "title": "Puma RS-X",
        "category": "Chaussure",
        "colors": ['noir', 'marron'],
        "sizes": [
            {
                '36': [
                    {'color': 'noir', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 8)},
                    {'color': 'marron', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 2)},
                ]
            },
            {
                '38': [
                    {'color': 'noir', 'oldPrice': 110, 'percent': 10, 'stock': random.randint(0, 20)},
                    {'color': 'marron', 'oldPrice': 110, 'percent': None, 'stock': random.randint(0, 28)},
                ]
            },
            {
                '39': [
                    {'color': 'noir', 'oldPrice': 120, 'percent': 10, 'stock': random.randint(0, 28)},
                    {'color': 'marron', 'oldPrice': 120, 'percent': None, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '41': [
                    {'color': 'noir', 'oldPrice': 120, 'percent': 10, 'stock': random.randint(0, 10)},
                    {'color': 'marron', 'oldPrice': 120, 'percent': None, 'stock': random.randint(0, 12)},
                ]
            },
            {
                '42': [
                    {'color': 'noir', 'oldPrice': 130, 'percent': 10, 'stock': random.randint(0, 1)},
                    {'color': 'marron', 'oldPrice': 130, 'percent': None, 'stock': random.randint(0, 4)},
                ]
            },
        ],
        "badge": "Nouveau",
        "tags": ["Textile", "Laine", "Mesh"],
        "brand": "Puma",
        "percent": 10,
        "price": 100,
        "stock": 28,
        "warranty": None,
        'imgDefault': 'images/shoes-8.png',
        'imgHover': 'images/shoes-3.png',
        "description": "La Puma RS-X incarne l'esprit rétro-futuriste des baskets des années 80 réinventées. Sa tige en mesh et textile assure une respirabilité optimale, renforcée par des inserts métalliques décoratifs. La semelle en caoutchouc épais offre une adhérence solide et un look massif tendance. Idéale pour les amateurs de sneakers à l'esthétique audacieuse, elle se décline en noir et marron. Parfaite pour un usage urbain, elle attire tous les regards.",
    },
    {
        "title": "Pull Adidas Essentials",
        "category": "Pull",
        "colors": ['gris', 'noir'],
        "sizes": [
            {
                'S': [
                    {'color': 'gris', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 8)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'M': [
                    {'color': 'gris', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 8)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 29)},
                ]
            },
            {
                'L': [
                    {'color': 'gris', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 8)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 22)},
                ]
            },
            {
                'XL': [
                    {'color': 'gris', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 8)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 32)},
                ]
            },
        ],
        "badge": "Collection",
        "tags": ["Coton", "Polyester", "Molletonné"],
        "brand": "Adidas",
        "percent": 15,
        "price": 70,
        "stock": 85,
        "warranty": None,
        'imgDefault': 'images/pull-2.png',
        'imgHover': 'images/pull-1.png',
        "description": "Le pull Adidas Essentials est un sweat à capuche molletonné qui allie confort et style urbain. Fabriqué en coton doux et polyester résistant, il conserve sa forme après de nombreux lavages. La capuche intégrée est réglable par cordon, et la poche kangourou avant permet de réchauffer ses mains. Parfait pour les journées fraîches, les séances de sport ou le télétravail, il se porte aussi bien en jogging qu'en jean. Un basique incontournable.",
    },
    {
        "title": "Sac Ludic",
        "category": "Sac",
        "colors": ['gris', 'noir'],
        "sizes": [
            {
                'unique': [
                    {'color': 'gris', 'oldPrice': None, 'percent': 18, 'stock': random.randint(0, 8)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 18, 'stock': random.randint(0, 20)},
                ]
            },
        ],
        "badge": "Collection",
        "brand": "Lacost",
        "tags": ["Cuir", "Textile", "Nylon"],
        "percent": 18,
        "price": 90,
        "stock": 40,
        "warranty": None,
        'imgDefault': 'images/bag-4.png',
        'imgHover': 'images/bag-2.png',
        "description": "Le sac Ludic est un sac à dos spacieux conçu pour le quotidien comme pour les voyages. Ses matériaux en polyester et nylon résistent à l'abrasion et aux petites pluies, tandis que le textile intérieur protège vos affaires. Des renforts en cuir synthétique aux points de pression augmentent la durabilité. Il dispose de multiples compartiments, dont une poche pour ordinateur 15 pouces. Léger et confortable, il se porte sans effort",
    },
    {
        "title": "Running Shorts Nike Flex",
        "category": "Short",
        "colors": ['noir', 'gris'],
        "sizes": [
            {
                'XS': [
                    {'color': 'gris', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 8)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'S': [
                    {'color': 'gris', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 8)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'M': [
                    {'color': 'gris', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 8)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'L': [
                    {'color': 'gris', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 8)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 20)},
                ]
            },
        ],
        "badge": None,
        "tags": ["Coton", "Elasthanne", "Spandex"],
        "brand": "Nike",
        "percent": 22,
        "price": 60,
        "stock": 55,
        "warranty": None,
        'imgDefault': 'images/short-2.png',
        'imgHover': 'images/short-3.png',
        "description": "Les Running Shorts Nike Flex sont spécialement conçus pour les coureurs cherchant légèreté et liberté. Le tissu en polyester et élasthanne évacue la transpiration et sèche rapidement, tandis que les panneaux en mesh optimisent la ventilation. Une doublure intégrée type caleçon évite de porter un sous-vêtement supplémentaire. La taille élastique avec cordon de serrage assure un ajustement parfait. Idéals pour le sprint ou le marathon, ils ne vous ralentiront pas.",
    },
    {
        "title": "T-shirt Adidas Essentials",
        "category": "T-shirt",
        "colors": ['blanc', 'noir'],
        "sizes": [
            {
                'S': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 18, 'stock': random.randint(0, 8)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'M': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 18, 'stock': random.randint(0, 8)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'L': [
                    {'color': 'noir', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'XL': [
                    {'color': 'noir', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 20)},
                    {'color': 'blanc', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 20)},
                ]
            },
        ],
        "badge": "Collection",
        "tags": ["Coton", "Elasthanne", "Spandex"],
        "brand": "Adidas",
        "percent": 18,
        "price": 65,
        "stock": 70,
        "warranty": None,
        'imgDefault': 'images/shirt-9.png',
        'imgHover': 'images/t-shirt-19.png',
        "description": "Ce t-shirt Adidas Essentials arbore un logo sérigraphié discret mais reconnaissable. Le mélange coton-polyester-élasthanne offre une douceur remarquable et une élasticité qui suit vos mouvements. Sa coupe droite classique convient à toutes les morphologies, et son col rond renforcé résiste à l'usure. Que ce soit pour le sport, le bureau décontracté ou les loisirs, ce t-shirt blanc ou noir deviendra vite un favori. Un excellent rapport qualité-prix.",
    },
    {
        "title": "Veste Puma Essentials",
        "category": "Pull",
        "colors": ['gris', 'noir', 'rouge'],
        "sizes": [
            {
                'S': [
                    {'color': 'rouge', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 20)},
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                    {'color': 'gris', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'M': [
                    {'color': 'rouge', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 20)},
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'L': [
                    {'color': 'rouge', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 20)},
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'XL': [
                    {'color': 'rouge', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 20)},
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                ]
            },
        ],
        "badge": "Nouveau",
        "brand": "Puma",
        "tags": ["Coton", "Elasthanne", "Spandex"],
        "percent": 25,
        "price": 110,
        "stock": 42,
        "warranty": None,
        'imgDefault': 'images/sweater.png',
        'imgHover': 'images/sweater-1.png',
        "description": "La veste Puma Essentials est en réalité un sweat zippé idéal pour les mi-saisons. Composée de polyester, élasthanne et nylon, elle protège du vent tout en restant respirante. La fermeture à zip plein longueur permet de réguler la température facilement. Les poignets et le bas sont côtelés pour conserver la chaleur. Parfaite pour le sport ou les sorties décontractées, elle existe en trois coloris : gris, noir et rouge. Une pièce polyvalente.",
    },
    {
        "title": "Ceinture Nike Reversible",
        "category": "Accessoire",
        "colors": ['noir', 'marron'],
        "sizes": [
            {
                'unique': [
                    {'color': 'noir', 'oldPrice': None, 'percent': 35, 'stock': random.randint(0, 20)},
                    {'color': 'marron', 'oldPrice': None, 'percent': 35, 'stock': random.randint(0, 20)},
                ]
            }
        ],
        "badge": "Promotion",
        "tags": ["Coton", "Textile", "Nylon"],
        "brand": "Luna",
        "percent": 35,
        "price": 40,
        "stock": 80,
        "warranty": None,
        'imgDefault': 'images/ceinture-1.png',
        'imgHover': 'images/ceinture.png',
        "description": "La ceinture Nike Reversible est un accessoire 2-en-1 malin : sa boucle rotative permet d'utiliser le cuir côté noir ou côté marron selon vos envies. La lanière en cuir véritable est renforcée par un textile intérieur pour plus de solidité. La boucle en métal brossé résiste à la corrosion. Idéale pour voyager léger, elle s'adapte aussi bien à un jean qu'à un pantalon de costume. Une promotion à ne pas manquer.",
    },
    {
        "title": "Sandale Tiffany",
        "category": "Accessoire",
        "colors": ['bleu', 'or'],
        "sizes": [
            {
                'unique': [
                    {'color': 'bleu', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 20)},
                    {'color': 'or', 'oldPrice': 70, 'percent': 22, 'stock': random.randint(0, 20)},
                ]
            }
        ],
        "badge": "Collection",
        "tags": ["Polyester", "Nylon", "Molletonné"],
        "brand": "Adidas",
        "percent": 20,
        "price": 45,
        "stock": 95,
        "warranty": None,
        'imgDefault': 'images/sandale.png',
        'imgHover': 'images/sandale-1.png',
        "description": "La sandale Tiffany est conçue pour les journées chaudes à la plage ou à la ville. Sa semelle extérieure en caoutchouc antidérapant assure une bonne accroche sur les surfaces mouillées. Le dessus en textile et synthétique est doux au contact, avec une bride ajustable pour un maintien personnalisé. Légère et résistante à l'eau, elle se nettoie facilement. Le coloris bleu et or apporte une touche estivale. Un accessoire pratique et stylé.",
    },
    {
        "title": "Nike Workers",
        "category": "T-shirt",
        "colors": ['gris', 'noir'],
        "sizes": [
            {
                'XS': [
                    {'color': 'gris', 'oldPrice': None, 'percent': 23, 'stock': random.randint(0, 20)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 23, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'S': [
                    {'color': 'bleu', 'oldPrice': None, 'percent': 23, 'stock': random.randint(0, 20)},
                    {'color': 'or', 'oldPrice': None, 'percent': 23, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'M': [
                    {'color': 'bleu', 'oldPrice': None, 'percent': 23, 'stock': random.randint(0, 20)},
                    {'color': 'or', 'oldPrice': 70, 'percent': 22, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'L': [
                    {'color': 'bleu', 'oldPrice': None, 'percent': 23, 'stock': random.randint(0, 20)},
                    {'color': 'or', 'oldPrice': None, 'percent': 23, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'XL': [
                    {'color': 'bleu', 'oldPrice': None, 'percent': 23, 'stock': random.randint(0, 20)},
                    {'color': 'or', 'oldPrice': None, 'percent': 23, 'stock': random.randint(0, 20)},
                ]
            },
        ],
        "badge": None,
        "tags": ["Rubber", "EVA", "Mesh"],
        "brand": "Nike",
        "percent": 23,
        "price": 40,
        "stock": 130,
        "warranty": None,
        'imgDefault': 'images/t-shirt-2.png',
        'imgHover': 'images/t-shirt-3.png',
        "description": "Le débardeur Nike Workers est taillé pour les entraînements intenses. Fabriqué en coton respirant, polyester évacuant l'humidité et élasthanne pour l'élasticité, il offre une grande liberté aux bras. Ses manches raglan augmentent l'amplitude des mouvements, parfait pour la musculation ou le crossfit. L'encolure en V est doublée pour éviter les déformations. Léger et séchant vite, il vous gardera au sec pendant vos efforts. Un indispensable du sporti",
    },
    {
        "title": "All Star",
        "category": "Sneakers",
        "colors": ['noir', 'rouge', 'bleu'],
        "sizes": [
            {
                '36': [
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                    {'color': 'rouge', 'oldPrice': None, 'percent': 30, 'stock': random.randint(0, 20)},
                    {'color': 'bleu', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '37': [
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                    {'color': 'rouge', 'oldPrice': None, 'percent': 30, 'stock': random.randint(0, 20)},
                    {'color': 'bleu', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '38': [
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                    {'color': 'rouge', 'oldPrice': None, 'percent': 30, 'stock': random.randint(0, 20)},
                    {'color': 'bleu', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '39': [
                    {'color': 'noir', 'oldPrice': None, 'percent': 5, 'stock': random.randint(0, 20)},
                    {'color': 'rouge', 'oldPrice': None, 'percent': 30, 'stock': random.randint(0, 20)},
                    {'color': 'bleu', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '40': [
                    {'color': 'noir', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 20)},
                    {'color': 'rouge', 'oldPrice': None, 'percent': 30, 'stock': random.randint(0, 20)},
                    {'color': 'bleu', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '42': [
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                    {'color': 'rouge', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                    {'color': 'bleu', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 20)},
                ]
            },
        ],
        "badge": "Collection",
        "tags": ["Elasthanne", "Mesh", "Textile"],
        "brand": "Converse",
        "percent": 30,
        "price": 95,
        "stock": 55,
        "warranty": None,
        'imgDefault': 'images/snearkes-1.png',
        'imgHover': 'images/snearkes-2.png',
        "description": "Les All Star de Converse sont des sneakers vintage au style indémodable. Leur tige en toile respirante est légère et résiste bien à l'usure quotidienne. La semelle extérieure en caoutchouc offre une adhérence classique, et les lacets plats renforcent le look rétro. Disponibles en noir, rouge et bleu, elles se marient avec tous les styles, du jean au short. Un must-have dans toute collection de chaussures urbaines.",
    },
    {
        "title": 'Platium lointine',
        "category": "Montre",
        "colors": None,
        "sizes": [
            {
                'unique': [
                    {'color': 'argent', 'oldPrice': None, 'percent': 15, 'stock': random.randint(0, 10)},
                ]
            }
        ] ,
        "badge": None,
        "tags": ["Molletonné", "Rubber", "Textile"],
        "brand": "Clementino",
        "percent": 15,
        "price": 390,
        "stock": 48,
        "warranty": 3,
        'imgDefault': 'images/watch-4.png',
        'imgHover': 'images/watch-5.png',
        "description": "La montre Platium lointine est une pièce classique en daim. Son boîtier en acier inoxydable brossé renferme un mouvement quartz précis. Le cadran est protégé par un verre minéral résistant aux rayures. Le bracelet en cuir véritable, beige ou marron, est fermé par une boucle déployante sécurisée. Parfaite pour un usage quotidien ou les occasions habillées, elle affiche une élégance sobre. Trois ans de garantie vous protègent.",
    },
    {
        "title": "Nike Deland",
        "category": "Short",
        "colors": ['gris', 'noir'],
        "sizes": [
            {
                'S': [
                    {'color': 'gris', 'oldPrice': None, 'percent': 18, 'stock': random.randint(0, 10)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 18, 'stock': random.randint(0, 10)},
                ]
            },
            {
                'M': [
                    {'color': 'gris', 'oldPrice': None, 'percent': 18, 'stock': random.randint(0, 10)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 18, 'stock': random.randint(0, 10)},
                ]
            },
            {
                'L': [
                    {'color': 'gris', 'oldPrice': None, 'percent': 18, 'stock': random.randint(0, 10)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 18, 'stock': random.randint(0, 10)},
                ]
            },

        ],
        "badge": None,
        "tags": ["Nylon", "Spandex", "Polyester"],
        "brand": "Noke",
        "percent": 18,
        "price": 40,
        "stock": 32,
        "warranty": None,
        'imgDefault': 'images/short-5.png',
        'imgHover': 'images/short-4.png',
        "description": "Le short Nike Deland, bien que sa description originale évoque une chaussure, est un short de sport performant. Composé de polyester, élasthanne et nylon, il résiste aux déchirures et sèche rapidement. Une poche zippée arrière permet de garder en sécurité vos clés ou carte. La taille élastique avec cordon ajustable assure un maintien parfait. Idéal pour le basket, la course ou la salle, il vous accompagne dans tous vos mouvements.",
    },
    {
        "title": "Pull Flamer display",
        "category": "Pull",
        "colors": ['gris', 'noir','violet'],
        "sizes": [
            {
                'S': [
                    {'color': 'gris', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 10)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 10)},
                    {'color': 'violet', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 10)},
                ]
            },
            {
                'M': [
                    {'color': 'gris', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 10)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 10)},
                    {'color': 'violet', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 10)},
                ]
            },
            {
                'L': [
                    {'color': 'gris', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 10)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 10)},
                    {'color': 'violet', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 10)},
                ]
            },
            {
                'XL': [
                    {'color': 'gris', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 10)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 10)},
                    {'color': 'violet', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 10)},
                ]
            },
        ],
        "badge": None,
        "tags": ["Coton", "Mesh", "Textile"],
        "brand": "Flamer",
        "percent": 22,
        "price": 160,
        "stock": 28,
        "warranty": None,
        'imgDefault': 'images/pull-4.png',
        'imgHover': 'images/pull-7.png',
        "description": "Le pull Flamer display est en réalité un sweat molletonné chaud et confortable. Fabriqué en coton doux, polyester résistant et molletonné épais, il retient la chaleur sans être trop lourd. Une poche kangourou avant pratique pour les mains. Les poignets et l'ourlet sont côtelés pour éviter les déformations. Parfait pour les journées fraîches ou les soirées cocooning, il se porte aussi bien à la maison qu'en ville. Un choix cosy.",
    },
    {
        "title": "Baskets Adidas ZX",
        "category": "Sneakers",
        "colors": ['blanc', 'noir'],
        "sizes": [
            {
                '36': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '37': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '38': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '39': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '40': [
                    {'color': 'blanc', 'oldPrice': 100, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': 100, 'percent': 20, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '43': [
                    {'color': 'blanc', 'oldPrice': 100, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': 100, 'percent': 20, 'stock': random.randint(0, 20)},
                ]
            },

        ],
        "badge": "Nouveau",
        "tags": ["Rubber", "Elasthanne", "Nylon"],
        "brand": "Adidas",
        "percent": 20,
        "price": 85,
        "stock": 58,
        "warranty": None,
        'imgDefault': 'images/sneaker-4.png',
        'imgHover': 'images/sneaker-5.png',
        "description": "Les baskets Adidas ZX réinterprètent un classique des années 80 avec des matériaux modernes. La tige en mesh et textile assure une respirabilité maximale, tandis que la semelle en caoutchouc offre une excellente accroche. Le système de laçage rapide permet de chausser en un geste. Le design blanc/noir est épuré et s'accorde avec tout. Parfaites pour le quotidien, elles allient confort et style rétro pour les amateurs de sneakers.",
    },
    {
        "title": "Luivitton Sky bord",
        "category": "Sac",
        "colors": ['marron', 'noir'],
        "sizes": [
            {
                'unique' : [
                    {'color': 'marron', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 30)},
                ]
            }
        ],
        "badge": "Edition",
        "tags": ["Elasthanne", "Mesh", "Textile"],
        "brand": "Luivitton",
        "percent": 10,
        "price": 2980,
        "stock": 8,
        "warranty": 5,
        'imgDefault': 'images/bac_lui.png',
        'imgHover': 'images/bag-1.png',
        "description": "Le sac Luivitton Sky bord est un article de prestige au design mécanique. Sa toile siglée résiste à l'eau et aux rayures, renforcée par des finitions en cuir de vachette naturelle. La serrure numérotée garantit la sécurité de vos effets personnels. Les garnitures en métal doré ajoutent une touche luxueuse. Idéal pour les voyages d'affaires, il dispose de plusieurs compartiments intérieurs. Livré avec une housse de protection.",
    },
    {
        'title': 'Converse  Taylor All Star',
        'category': 'Sneakers',
        'colors': ['blanc', 'noir'],
        'sizes': [
            {
                '36': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                ]
            },
            {
                '37': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                ]
            },
            {
                '40': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                ]
            },
            {
                '41': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                ]
            },
            {
                '42': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                ]
            },
        ],
        'tags': ['Textile', 'Rubber', 'Coton'],
        'badge': 'Collection',
        'brand': 'Converse',
        'percent': 20,
        'price': 65,
        'stock': 72,
        'warranty': None,
        'imgDefault': 'images/sneaker-3.png',
        'imgHover': 'images/sneaker-6.png',
        'description':  "Les Converse Taylor All Star sont des baskets iconiques reconnues mondialement. Leur tige en toile résistante est légère et facile d'entretien. La semelle en caoutchouc vulcanisé offre une adhérence et une durabilité légendaires. Le patch logo rond sur la cheville est l'emblème de la marque. Parfaites pour le skate, le rock ou la vie de tous les jours, elles apportent une touche décontractée à toutes vos tenues. Un grand classique.",
    },
    {
        'title': 'New Balance 574',
        'category': 'Sneakers',
        'colors': ['gris', 'noir', 'blanc'],
        'sizes': [
            {
                '36': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 20)},
                    {'color': 'gris', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 10)},
                ]
            },
            {
                '37': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 20)},
                    {'color': 'gris', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 10)},
                ]
            },
            {
                '38': [
                    {'color': 'blanc', 'oldPrice': 120, 'percent': 25, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': 120, 'percent': 25, 'stock': random.randint(0, 20)},
                    {'color': 'gris', 'oldPrice': 120, 'percent': 25, 'stock': random.randint(0, 10)},
                ]
            },
            {
                '41': [
                    {'color': 'blanc', 'oldPrice': 120, 'percent': 25, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': 120, 'percent': 25, 'stock': random.randint(0, 20)},
                    {'color': 'gris', 'oldPrice': 120, 'percent': 25, 'stock': random.randint(0, 10)},
                ]
            },
            {
                '42': [
                    {'color': 'blanc', 'oldPrice': 120, 'percent': 25, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': 120, 'percent': 25, 'stock': random.randint(0, 20)},
                    {'color': 'gris', 'oldPrice': 120, 'percent': 25, 'stock': random.randint(0, 10)},
                ]
            },
        ],
        'tags': ['Mesh', 'Rubber', 'EVA'],
        'badge': 'Nouveau',
        'brand': 'New Balance',
        'percent': 25,
        'price': 110,
        'stock': 58,
        'warranty': None,
        'imgDefault': 'images/sneakers-3.png',
        'imgHover': 'images/sneakers-4.png',
        'description': "La New Balance 574 est une sneaker confortable pour la marche quotidienne. Sa tige en mesh assure une respirabilité optimale, tandis que la semelle EVA offre un amorti moelleux. La technologie ENCAP associe un noyau en EVA à un bord en caoutchouc pour un soutien durable. Disponible en gris, noir ou blanc, cette chaussure s'adapte à tous les pieds. Parfaite pour le travail ou les balades, elle allie tradition et modernit",
    },
    {
        'title': 'Vans Old Skool',
        'category': 'Sneakers',
        'colors': ['noir', 'blanc'],
        'sizes': [
            {
                '37': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '38': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '40': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 22, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '41': [
                    {'color': 'blanc', 'oldPrice': 85, 'percent': 22, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': 85, 'percent': 22, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '42': [
                    {'color': 'blanc', 'oldPrice': 85, 'percent': 22, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': 85, 'percent': 22, 'stock': random.randint(0, 20)},
                ]
            },

        ],
        'tags': ['Textile', 'Rubber', 'Nylon'],
        'badge': 'Promotion',
        'brand': 'Vans',
        'percent': 22,
        'price': 75,
        'stock': 65,
        'warranty': None,
        'imgDefault': 'images/sneaker-9.png',
        'imgHover': 'images/sneaker-10.png',
        'description': "Les Vans Old Skool sont des chaussures de skateboard au design légendaire. La tige en toile et suède résiste aux abrasions du grip. La semelle en caoutchouc waffle offre une adhérence exceptionnelle. La stripe latérale décorative est devenue un signe distinctif. Avec leurs lacets plats et leur col renforcé, elles tiennent bien au pied. Parfaites pour rider ou pour un look streetwear, elles ne se démodent jamais.",
    },
    {
        'title': 'T-Shirt Lacoste Basic',
        'category': 'T-shirt',
        'colors': ['blanc', 'noir'],
        'sizes': [
            {
                'XS': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 30, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 30, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'S': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 30, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 30, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'M': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 30, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 30, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'L': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 30, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 30, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'XL': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 30, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 30, 'stock': random.randint(0, 20)},
                ]
            },
        ],
        'tags': ['Coton', 'Elasthanne', 'Textile'],
        'badge': 'Collection',
        'brand': 'Lacoste',
        'percent': 30,
        'price': 55,
        'stock': 95,
        'warranty': None,
        'imgDefault': 'images/t-shirt-7.png',
        'imgHover': 'images/t-shirt-8.png',
        'description': "Le t-shirt Lacoste Basic est un incontournable du dressing chic-décontracté. Fabriqué en coton peigné, polyester et élasthanne, il offre une souplesse et une tenue parfaite. Le célèbre petit crocodile vert est brodé sur la poitrine. La coupe est droite et les manches courtes sont adaptées à toutes les morphologies. Disponible en blanc ou noir, il se porte aussi bien avec un bermuda qu'avec un jean. Un classique indémodable.",
    },
    {
        'title': 'T-Shirt Tommy Hilfiger',
        'category': 'T-shirt',
        'colors': ['blanc', 'rouge'],
        'sizes': [
            {
                'S': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'rouge', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'M': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'rouge', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'L': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'rouge', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'XL': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 30)},
                    {'color': 'rouge', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'XXL': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 30)},
                    {'color': 'rouge', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                ]
            },
        ],
        'tags': ['Coton', 'Polyester', 'Elasthanne'],
        'badge': 'Nouveau',
        'brand': 'Tommy Hilfiger',
        'percent': 20,
        'price': 50,
        'stock': 88,
        'warranty': None,
        'imgDefault': 'images/t-shirt-9.png',
        'imgHover': 'images/t-shirt-10.png',
        'description': "Ce t-shirt Tommy Hilfiger arbore le drapeau américain embroché sur la manche. Le mélange coton, polyester et élasthanne assure confort et élasticité. Sa coupe classique est agrémentée d'un col rond en côtes. Le coloris blanc ou rouge est vif et résiste bien aux lavages. Idéal pour un look preppy moderne, il se marie parfaitement avec un short ou un pantalon chino. Un basique de qualité supérieure.",
    },
    {
        'title': 'T-Shirt Calvin Klein',
        'ref': 'CAL001',
        'category': 'T-shirt',
        'colors': ['noir', 'blanc', 'gris'],
        'sizes': [
            {
                'XS': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 30)},
                    {'color': 'gris', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'S': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 30)},
                    {'color': 'gris', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'M': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 30)},
                    {'color': 'gris', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'L': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 30)},
                    {'color': 'gris', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'XL': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 30)},
                    {'color': 'gris', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 20)},
                ]
            },

        ],
        'tags': ['Coton', 'Elasthanne', 'Textile'],
        'badge': None,
        'brand': 'Calvin Klein',
        'percent': 25,
        'price': 60,
        'stock': 110,
        'warranty': None,
        'imgDefault': 'images/t-shirt-11.png',
        'imgHover': 'images/t-shirt-8.png',
        'description': "Le t-shirt Calvin Klein minimaliste mise sur des matières nobles : coton, modal doux et élasthanne. L'étiquette extérieure reprend le logo emblématique. La coupe ajustée sans être moulante flatte la silhouette. Disponible en noir, blanc ou gris, il constitue la base parfaite pour toute tenue. Que ce soit sous une veste ou porté seul, ce t-shirt respire le luxe discret. Une pièce polyvalente et durable.",
    },
    {
        'title': 'Asics Gel-Lyte III',
        'category': 'Chaussure',
        'colors': ['gris', 'noir'],
        'sizes': [
            {
                '36': [
                    {'color': 'noir', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 30)},
                    {'color': 'gris', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '37': [
                    {'color': 'noir', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 30)},
                    {'color': 'gris', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '38': [
                    {'color': 'noir', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 30)},
                    {'color': 'gris', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '41': [
                    {'color': 'noir', 'oldPrice': 150, 'percent': None, 'stock': random.randint(0, 30)},
                    {'color': 'gris', 'oldPrice': 150, 'percent': None, 'stock': random.randint(0, 20)},
                ]
            },
            {
                '42': [
                    {'color': 'noir', 'oldPrice': 150, 'percent': None, 'stock': random.randint(0, 30)},
                    {'color': 'gris', 'oldPrice': 150, 'percent': None, 'stock': random.randint(0, 20)},
                ]
            },

        ],
        'tags': ['Rubber', 'Mesh', 'Cuir'],
        'badge': 'Edition',
        'brand': 'Asics',
        'percent': None,
        'price': 130,
        'stock': 42,
        'warranty': None,
        'imgDefault': 'images/shoe-5.png',
        'imgHover': 'images/shoe-7.png',
        'description': "La Asics Gel-Lyte III est une chaussure rétro running très recherchée. Sa tige en mesh et suède offre respirabilité et look vintage. Le système Gel à l'arrière amortit les impacts efficacement. La semelle extérieure en caoutchouc assure une adhérence sûre sur route. Avec son empeigne divisée qui s'adapte au pied, elle est idéale pour un usage quotidien ou la course légère. Un modèle culte qui traverse les époques.",
    },
    {
        'title': 'Reebok Classic Leather',
        'category': 'Chaussure',
        'colors': ['blanc', 'noir'],
        'sizes': [
            {
                '36': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 35, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 35, 'stock': random.randint(0, 30)},
                ]
            },
            {
                '38': [
                    {'color': 'blanc', 'oldPrice': None, 'percent': 35, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 35, 'stock': random.randint(0, 30)},
                ]
            },
             {
                '40': [
                    {'color': 'blanc', 'oldPrice': 90, 'percent': 35, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 35, 'stock': random.randint(0, 30)},
                ]
            },
             {
                '41': [
                    {'color': 'blanc', 'oldPrice': 90, 'percent': 35, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 30)},
                ]
            },
             {
                '42': [
                    {'color': 'blanc', 'oldPrice': 90, 'percent': 35, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 30)},
                ]
            },
        ],
        'tags': ['Cuir', 'Rubber', 'Textile'],
        'badge': 'Promotion',
        'brand': 'Reebok',
        'percent': 35,
        'price': 85,
        'stock': 54,
        'warranty': 2,
        'imgDefault': 'images/shoes-10.png',
        'imgHover': 'images/shoes-9.png',
        'description': "La Reebok Classic Leather est une chaussure intemporelle au look sobre. Sa tige en cuir blanc ou noir est facile à entretenir et résiste bien. La doublure intérieure en mousse offre un confort moelleux. La semelle extérieure en caoutchouc garantit une bonne adhérence. Parfaite pour un style casual, elle s'associe avec un jean, un chino ou même un short. Deux ans de garantie vous protègent contre les défauts de fabrication. Un classique abordable.",
    },
    {
        'title': 'Manteau Mango Wool',
        'category': 'Manteaux',
        'colors': ['marron', 'noir', 'gris'],
        'sizes': [
            {
                'S': [
                    {'color': 'marron', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'gris', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                ]
            },
             {
                'M': [
                    {'color': 'marron', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'gris', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 30)},
                ]
            },
             {
                'L': [
                    {'color': 'marron', 'oldPrice': 175, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': 168, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'gris', 'oldPrice': 165, 'percent': 20, 'stock': random.randint(0, 30)},
                ]
            },
             {
                'XL': [
                    {'color': 'marron', 'oldPrice': 180, 'percent': 20, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': 175, 'percent': 20, 'stock': random.randint(0, 30)},
                ]
            },
        ],
        'tags': ['Laine', 'Polyester', 'Nylon'],
        'badge': 'Nouveau',
        'brand': 'Mango',
        'percent': 20,
        'price': 160,
        'stock': 38,
        'warranty': None,
        'imgDefault': 'images/coat-5.png',
        'imgHover': 'images/coat-5.png',
        'description': "Le manteau Mango Wool est un vêtement élégant pour l'automne et l'hiver. Sa composition laine, polyester et nylon le rend chaud sans être trop lourd. La doublure intérieure satinée glisse facilement sur les vêtements. La coupe droite et les poches latérales sont à la fois pratiques et stylées. Disponible en marron, noir ou gris, il s'adapte aussi bien au bureau qu'aux sorties. Un manteau de qualité qui durera des années.",
    },
    {
        'title': 'Manteau Zara Minimalist',
        'category': 'Manteaux',
        'colors': ['noir', 'beige'],
        'sizes': [
            {
                'XS': [
                    {'color': 'noir', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 30)},
                    {'color': 'beige', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 30)},
                ]
            },
            {
                'S': [
                    {'color': 'noir', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 30)},
                    {'color': 'beige', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 30)},
                ]
            },
            {
                'M': [
                    {'color': 'noir', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 30)},
                    {'color': 'beige', 'oldPrice': None, 'percent': 25, 'stock': random.randint(0, 30)},
                ]
            },
            {
                'L': [
                    {'color': 'noir', 'oldPrice': 150, 'percent': 15, 'stock': random.randint(0, 30)},
                    {'color': 'beige', 'oldPrice': 150, 'percent': 15, 'stock': random.randint(0, 30)},
                ]
            },
            {
                'XL': [
                    {'color': 'noir', 'oldPrice': 150, 'percent': 15, 'stock': random.randint(0, 30)},
                    {'color': 'beige', 'oldPrice': 150, 'percent': 15, 'stock': random.randint(0, 30)},
                ]
            },
        ],
        'tags': ['Polyester', 'Nylon', 'Laine'],
        'badge': None,
        'brand': 'Zara',
        'percent': 25,
        'price': 140,
        'stock': 45,
        'warranty': None,
        'imgDefault': 'images/coat-8.png',
        'imgHover': 'images/coat-7.png',
        'description': "Le manteau Zara Minimalist est épuré et moderne. Sa composition polyester, nylon et laine le rend résistant au vent et à l'eau. Une ceinture assortie permet de marquer la taille pour une silhouette féminine ou masculine. Les boutons dissimulés donnent un look très propre. Idéal pour les looks minimalistes, il se porte aussi bien sur une robe que sur un costume. Un investissement mode intelligent.",
    },
    {
        'title': 'Chemise Ralph Lauren Oxford',
        'category': 'Chemise',
        'colors': ['bleu'],
        'sizes': [
            {
                'S': [
                    {'color': 'bleu', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 30)},
                ]
            },
             {
                'M': [
                    {'color': 'bleu', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 30)},
                ]
            },
             {
                'L': [
                    {'color': 'bleu', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 30)},
                    {'color': 'beige', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 30)},
                ]
            },
             {
                'XL': [
                    {'color': 'noir', 'oldPrice': 115, 'percent': None, 'stock': random.randint(0, 30)},
                    {'color': 'beige', 'oldPrice': 115, 'percent': None, 'stock': random.randint(0, 30)},
                ]
            },
             {
                'XXL': [
                    {'color': 'noir', 'oldPrice': 120, 'percent': None, 'stock': random.randint(0, 30)},
                    {'color': 'beige', 'oldPrice': 120, 'percent': None, 'stock': random.randint(0, 30)},
                ]
            },
        ],
        'tags': ['Coton', 'Polyester', 'Soie'],
        'badge': 'Edition',
        'brand': 'Ralph Lauren',
        'percent': 10,
        'price': 95,
        'stock': 62,
        'warranty': None,
        "imgDefault": "images/shirt-5.png",
        "imgHover": "images/shirt-4.png",
        'description': "La chemise Ralph Lauren Oxford est un symbole de l'élégance américaine. Taillée dans du coton Oxford, avec un peu de polyester et d'élasthanne pour le confort, elle résiste aux froissements. Le logo du cheval et du joueur de polo est finement brodé sur la poitrine. Sa couleur bleue est intemporelle, et sa coupe régulière convient à toutes les morphologies. Parfaite pour le travail ou les dîners, elle ne se démodera jamais.",
    },
    {
        'title': 'Chemise Burberry Nova Check',
        'category': 'Chemise',
        'colors': ['rouge', 'noir'],
        'sizes': [
            {
                'S': [
                    {'color': 'rouge', 'oldPrice': None, 'percent': 8, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 8, 'stock': random.randint(0, 30)},
                ]
            },
            {
                'M': [
                    {'color': 'rouge', 'oldPrice': None, 'percent': 8, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 8, 'stock': random.randint(0, 30)},
                ]
            },
            {
                'L': [
                    {'color': 'rouge', 'oldPrice': None, 'percent': 8, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 8, 'stock': random.randint(0, 30)},
                ]
            },
            {
                'XL': [
                    {'color': 'rouge', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': 10, 'stock': random.randint(0, 30)},
                ]
            },
        ],
        'tags': ['Coton', 'Soie', 'Elasthanne'],
        'badge': 'Nouveau',
        'brand': 'Burberry',
        'percent': 8,
        'price': 180,
        'stock': 28,
        'warranty': None,
        'imgDefault': 'images/shirt-7.png',
        'imgHover': 'images/shirt-6.png',
        'description': "La chemise Burberry Nova Check affiche le célèbre motif écossais revisité. Confectionnée en coton, soie et élasthanne, elle allie noblesse et élasticité. Les couleurs rouge et noir contrastent élégamment. La coupe est ajustée, avec des poignets mousquetaires. Parfaite pour les occasions spéciales ou pour affirmer son style chic, cette chemise luxueuse est un véritable atout. Le motif Nova reste un classique de la maison britannique.",
    },
    {
        'title': 'Pull Gucci Wool',
        'category': 'Pull',
        'sizes': [
            {
                'XS': [
                    {'color': 'beige', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 30)},
                ]
            },
            {
                'S': [
                    {'color': 'beige', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 30)},
                ]
            },
            {
                'M': [
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 30)},
                ]
            },
            {
                'L': [
                    {'color': 'beige', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 30)},
                ]
            },
            {
                'XL': [
                    {'color': 'beige', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 30)},
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 30)},
                ]
            },
        ],
        'tags': ['Laine', 'Soie', 'Coton'],
        'badge': 'Edition',
        'brand': 'Gucci',
        'percent': None,
        'price': 250,
        'stock': 18,
        'warranty': None,
        'imgDefault': 'images/pull-5.png',
        'imgHover': 'images/pull-6.png',
        'description': "Le pull Stella McCartney est conçu dans une démarche écoresponsable, avec de la laine recyclée, du coton biologique et de l'élasthanne. Sa coupe épurée en fait un basique luxueux. Disponible en gris ou noir, il se marie avec tout. Les finitions sont impeccables, sans logo apparent. Idéal pour ceux qui allient mode et conscience environnementale. Une promotion rend ce produit encore plus accessible. Un choix engagé."
    },
    {
        'title': 'Pull Stella McCartney',
        'category': 'Pull',
        'colors': ['gris', 'noir'],
        'sizes': [
            {
                'S': [
                    {'color':'gris','oldPrice': None,'percent': 22,'stock':random.randint(0,10)},
                    {'color':'noir','oldPrice': None,'percent': 22,'stock':random.randint(0,10)}
                ]
            },
            {
                'M': [
                    {'color':'gris','oldPrice': None,'percent': 22,'stock':random.randint(0,10)},
                    {'color':'noir','oldPrice':'','percent': 22,'stock':random.randint(0,10)}
                ]
            },
            {
                'L': [
                    {'color':'gris','oldPrice': None,'percent': 22,'stock':random.randint(0,10)},
                    {'color':'noir','oldPrice':'','percent': 22,'stock':random.randint(0,10)}
                ]
            },
            {
                'XL': [
                    {'color':'gris','oldPrice': None,'percent': 22,'stock':random.randint(0,10)},
                    {'color':'noir','oldPrice':'','percent': 22,'stock':random.randint(0,10)}
                ]
            },
             {
                'XXL': [
                    {'color':'gris','oldPrice': None,'percent': 22,'stock':random.randint(0,10)},
                    {'color':'noir','oldPrice':'','percent': 22,'stock':random.randint(0,10)}
                ]
            },

        ],
        'tags': ['Laine', 'Coton', 'Elasthanne'],
        'badge': 'Promotion',
        'brand': 'Stella McCartney',
        'price': 180,
        'warranty': None,
        'description': 'Pull luxe et durable',
        'imgDefault': 'images/pull-5.png',
        'imgHover': 'images/pull-6.png',
    },
    {
        'title': 'Short Adidas Climalite',
        'category': 'Short',
        'colors': ['noir', 'blanc'],
        'sizes': [
            {
                'XS': [
                    {'color':'noir','oldPrice': None,'percent': 40,'stock':random.randint(0,10)},
                    {'color':'blanc','oldPrice': None,'percent': 40,'stock':random.randint(0,10)}
                ]
            },
            {
                'S': [
                    {'color':'noir','oldPrice': None,'percent': 40,'stock':random.randint(0,10)},
                    {'color':'blanc','oldPrice': None,'percent': 40,'stock':random.randint(0,10)}
                ]
            },
            {
                'M': [
                    {'color':'noir','oldPrice': None,'percent': 40,'stock':random.randint(0,10)},
                    {'color':'blanc','oldPrice': None,'percent': 40,'stock':random.randint(0,10)}
                ]
            },
            {
                'L': [
                    {'color':'noir','oldPrice': None,'percent': 40,'stock':random.randint(0,10)},
                    {'color':'blanc','oldPrice': None,'percent': 40,'stock':random.randint(0,10)}
                ]
            },
            {
                'XL': [
                    {'color':'noir','oldPrice': None,'percent': 40,'stock':random.randint(0,10)},
                    {'color':'blanc','oldPrice': None,'percent': 40,'stock':random.randint(0,10)}
                ]
            },
        ],
        'tags': ['Polyester', 'Elasthanne', 'Mesh'],
        'badge': 'Collection',
        'brand': 'Adidas',
        'percent': 40,
        'price': 60,
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
        'sizes': [
            {
                'unique': [
                    {'color':'noir','oldPrice': None,'percent': 30,'stock':random.randint(0,20)},
                    {'color':'rouge','oldPrice': None,'percent': None,'stock':random.randint(0,20)},
                ]
            }
        ],
        'tags': ['Cuir', 'Textile', 'Caoutchouc'],
        'badge': 'Edition',
        'brand': 'Gucci',
        'price': 450,
        'warranty': 2,
        'description': 'Sac à main de luxe',
        'imgDefault': 'images/bag.png',
        'imgHover': 'images/bag-3.png',
    },
    {
        'title': 'Sac Louis Vuitton Neverfull',
        'category': 'Sac',
        'colors': ['marron', 'noir'],
        'sizes': [
            {
                'unique' : [
                    {'color':'noir','oldPrice': None,'percent': None,'stock':random.randint(0,20)},
                    {'color':'marron','oldPrice': None,'percent': None,'stock':random.randint(0,20)},
                ]
            }
        ],
        'tags': ['Cuir', 'Textile', 'Monogram'],
        'badge': 'Nouveau',
        'brand': 'Louis Vuitton',
        'price': 1200,
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
        'sizes': [
            {
                'unique': [
                    {'color': 'rouge', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                ]
            }
        ],
        'tags': ['Soie', 'Textile', 'Caoutchouc'],
        'badge': 'Edition',
        'brand': 'Hermès',
        'price': 100,
        'warranty': None,
        'description': 'Foulard en soie de prestige',
        'imgDefault': 'images/scarf.png',
        'imgHover': 'images/scarf-1.png',
    },
    {
        'title': 'Costume Versace Silk',
        'category': 'Costume',
        'colors': ['noir', 'bleu'],
        'sizes': [
            {
               'S': [
                    {'color':'noir','oldPrice': None,'percent': 15,'stock':random.randint(0,20)},
               ]
            },
            {
               'M': [
                    {'color':'noir','oldPrice': 1550,'percent': 15,'stock':random.randint(0,20)},
               ]
            },
            {
               'L': [
                    {'color':'noir','oldPrice': 1600,'percent': 15,'stock':random.randint(0,20)},
               ]
            },
            {
               'XL': [
                    {'color':'noir','oldPrice': 1700,'percent': 15,'stock':random.randint(0,20)},
               ]
            },

        ],
        'tags': ['Soie', 'Laine', 'Polyester'],
        'badge': 'Edition',
        'brand': 'Versace',
        'price': 1500,
        'warranty': None,
        'description': 'Costume de prestige en soie',
        'imgDefault': 'images/coat.png',
        'imgHover': 'images/coat-2.png',
    },
    {
        'title': 'Montre Rolex Datejust',
        'category': 'Montre',
        'sizes': [
            {
                'unique' : [
                    {'color':'argent','oldPrice': None,'percent': None,'stock':random.randint(0,3)},
                    {'color':'or','oldPrice': None,'percent': None,'stock':random.randint(0,3)},
                ]
            }
        ],
        'tags': ['Acier', 'Or', 'Cristal', 'Saphir'],
        'badge': 'Edition',
        'brand': 'Rolex',
        'price': 5500,
        'warranty': 6,
        'description': 'Montre de prestige légendaire',
        'imgDefault': 'images/watch-3.png',
        'imgHover': 'images/watch-4.png',
    },
    {
        'title': 'Liquid Sweater',
        'category': 'Pull',
        'sizes': [
            {
                'S' : [
                    {'color':'noir','oldPrice': None,'percent': None,'stock':random.randint(0,20)},
                    {'color':'gris','oldPrice': None,'percent': None,'stock':random.randint(0,20)},
                ]
            },
            {
                'M' : [
                    {'color':'noir','oldPrice': 160,'percent': None,'stock':random.randint(0,20)},
                    {'color':'gris','oldPrice': 160,'percent': None,'stock':random.randint(0,20)},
                ]
            },
            {
                'L' : [
                    {'color':'noir','oldPrice': 170,'percent': None,'stock':random.randint(0,20)},
                    {'color':'gris','oldPrice': 170,'percent': None,'stock':random.randint(0,20)},
                ]
            },
            {
                'XL' : [
                    {'color':'noir','oldPrice': 175,'percent': None,'stock':random.randint(0,20)},
                    {'color':'gris','oldPrice': 175,'percent': None,'stock':random.randint(0,20)},
                    {'color':'vert','oldPrice': 175,'percent': None,'stock':random.randint(0,20)},
                ]
            },

        ],
        'tags': ['Coton', 'Polyester', 'Soie'],
        'badge': 'Edition',
        'brand': 'Nike',
        'price': 150,
        'warranty': None,
        'description': 'Liquid Sweater de l\'élégance et classe',
        'imgDefault': 'images/sweater-4.png',
        'imgHover': 'images/sweater-4.png',
    },
    {
        'title': 'La gardène le roi',
        'category': 'Pull',
        'sizes': [
            {
                'S' : [
                    {'color':'gris','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
                    {'color':'noir','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
                    {'color':'rose','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
                ],
            },
            {
                'M' :[
                    {'color':'gris','oldPrice': 255,'percent': 20,'stock':random.randint(0,20)},
                    {'color':'noir','oldPrice': 255,'percent': 20 ,'stock':random.randint(0,20)},
                    {'color':'rose','oldPrice': 255,'percent': 20,'stock':random.randint(0,20)},
                ],
            },
            {
                'L' : [
                    {'color':'gris','oldPrice': 260,'percent': 20,'stock':random.randint(0,20)},
                    {'color':'noir','oldPrice': 260,'percent': 20,'stock':random.randint(0,20)},
                    {'color':'rose','oldPrice': 260,'percent': 20,'stock':random.randint(0,20)},
                ],
            },
            {
                'XL' : [
                    {'color':'gris','oldPrice': 260,'percent': 10,'stock':random.randint(0,20)},
                    {'color':'noir','oldPrice': 260,'percent': 10,'stock':random.randint(0,20)},
                    {'color':'rose','oldPrice': 260,'percent': 10,'stock':random.randint(0,20)},
                ],
            },
        ],
        'tags': ['Coton', 'Spandex', 'Soie'],
        'badge': 'Collection',
        'brand': 'Adidas',
        'price': 250,
        'warranty': None,
        'description': 'Liquid Sweater de l\'élégance et classe',
        'imgDefault': 'images/sweater-6.png',
        'imgHover': 'images/sweater-7.png',
    },
    {
        'title': 'Polo craque',
        'category': 'Pull',
        'sizes': [
            {
                'S': [
                    {'color':'bleu','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
                    {'color':'noir','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
                    {'color':'violet','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
                ]
            },
            {
                'M': [
                    {'color':'bleu','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
                    {'color':'gris','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
                    {'color':'violet','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
                ]
            },
            {
                'L': [
                    {'color':'noir','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
                    {'color':'bleu','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
                    {'color':'gris','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
                    {'color':'violet','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
                ]
            },
            {
                'XL': [
                    {'color':'noir','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
                    {'color':'bleu','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
                    {'color':'gris','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
                    {'color':'violet','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
                ]
            },
        ],
        'tags': ['Coton', 'Molletonné', 'Textile'],
        'badge': None,
        'brand': 'La croix',
        'price': 60,
        'warranty': None,
        'description': 'Liquid Sweater de l\'élégance et classe',
        'imgDefault': 'images/t-shirt-13.png',
        'imgHover': 'images/t-shirt-14.png',
    },
    {
        'title': 'Charlotte platinelle',
        'category': 'Chaussure',
        'sizes': [
            {
                '36': [
                    {'color':'argent','oldPrice': None,'percent': 25,'stock':random.randint(0,10)},
                    {'color':'noir','oldPrice': None,'percent': 25,'stock':random.randint(0,10)},
                ]
            },
            {
                '38': [
                    {'color':'argent','oldPrice': None,'percent': 25,'stock':random.randint(0,10)},
                ]
            },
            {
                '39': [
                    {'color':'argent','oldPrice': None,'percent': 25,'stock':random.randint(0,10)},
                    {'color':'noir','oldPrice': None,'percent': 25,'stock':random.randint(0,10)},
                ]
            },
            {
                '40': [
                    {'color':'argent','oldPrice': None,'percent': 25,'stock':random.randint(0,10)},
                    {'color':'noir','oldPrice': None,'percent': 25,'stock':random.randint(0,10)},
                ]
            },
        ],
        'tags': ['Cristal', 'EVA', 'Saphir'],
        'badge': 'Collection',
        'brand': 'Nicoles Autain',
        'price': 460,
        'warranty': 4,
        'description': 'Charlotte platinelle la mode à la parisiènne',
        'imgDefault': 'images/shoes-13.png',
        'imgHover': 'images/shoes-12.png',
    },
    {
        'title': 'Weston larmard',
        'category': 'Chaussure',
        'sizes': [
            {
                '39': [
                    {'color':'argent','oldPrice': None,'percent': 25,'stock':random.randint(0,10)},
                    {'color':'marron','oldPrice': None,'percent': 25,'stock':random.randint(0,10)}
                ]
            },
            {
                '41': [
                    {'color':'argent','oldPrice': None,'percent': 25,'stock':random.randint(0,10)},
                    {'color':'marron','oldPrice': None,'percent': 25,'stock':random.randint(0,10)}
                ]
            },
            {
                '42': [
                    {'color':'argent','oldPrice': None,'percent': 25,'stock':random.randint(0,10)},
                    {'color':'marron','oldPrice': None,'percent': 25,'stock':random.randint(0,10)}
                ]
            },
            {
                '45': [
                    {'color':'argent','oldPrice': 600,'percent': 25,'stock':random.randint(0,10)},
                    {'color':'marron','oldPrice': 600,'percent': 25,'stock':random.randint(0,10)}
                ]
            },
        ],
        'tags': ['Cuir', 'Mesh', 'Monogram'],
        'badge': None,
        'brand': 'Nicoles Autain',
        'price': 570,
        'warranty': None,
        'description': 'Weston larmard le luxe en éclat de verre',
        'imgDefault': 'images/shoes-14.png',
        'imgHover': 'images/shoes-10.png',
    },
    {
        'title': 'Armer cold',
        'category': 'Pull',
        'sizes': [
            {
                'S' : [
                    {'color':'vert','oldPrice': None,'percent': 15,'stock':random.randint(0,10)},
                    {'color':'noir','oldPrice': None,'percent': 15,'stock':random.randint(0,10)},
                ]
            },
            {
                'M' : [
                    {'color':'vert','oldPrice': 330,'percent': 15,'stock':random.randint(0,10)},
                    {'color':'noir','oldPrice': 330,'percent': 15,'stock':random.randint(0,10)},
                ]
            },
            {
                'L' : [
                    {'color':'vert','oldPrice': 330,'percent': 15,'stock':random.randint(0,10)},
                    {'color':'noir','oldPrice': 330,'percent': 15,'stock':random.randint(0,10)},
                ]
            },

        ],
        'tags': ['Textile', 'Soie', 'Laine'],
        'badge': 'Collection',
        'brand': 'Nicoles Autain',
        'price': 300,
        'warranty': None,
        'description': 'Armer cold pull confortable',
        'imgDefault': 'images/coat-9.png',
        'imgHover': 'images/coat-10.png',
    },
    {
        'title': 'Dyson shirt close',
        'category': 'Chemise',
        'sizes': [
            {
                'S': [
                    {'color':'ciel','oldPrice': None,'percent': 35,'stock':random.randint(0,10)},
                    {'color':'bleu','oldPrice': None,'percent': 35,'stock':random.randint(0,10)},
                ]
            },
            {
                'M': [
                    {'color':'ciel','oldPrice': None,'percent': 35,'stock':random.randint(0,10)},
                    {'color':'bleu','oldPrice': None,'percent': 35,'stock':random.randint(0,10)},
                ]
            },
            {
                'L': [
                    {'color':'ciel','oldPrice': None,'percent': 35,'stock':random.randint(0,10)},
                    {'color':'bleu','oldPrice': None,'percent': 35,'stock':random.randint(0,10)},
                ]
            },
        ],
        'tags': ['Coton', 'Laine', 'Monogram'],
        'badge': None,
        'brand': 'Lucas',
        'price': 120,
        'warranty': None,
        'description': 'Dyson shirt close chemise de haute qualité et d\'expertise de luxe',
        'imgDefault': 'images/shirt-13.png',
        'imgHover': 'images/shirt-23.png',
    },
    {
        'title': 'Dynamique Hawai lunaire',
        'category': 'Chemise',
        'colors': ['ciel', 'bleu'],
        'sizes': [
            {
                'S': [
                    {'color':'ciel','oldPrice': None,'percent': 50,'stock':random.randint(0,10)},
                    {'color':'bleu','oldPrice': None,'percent': 50,'stock':random.randint(0,10)},
                ]
            },
            {
                'M': [
                    {'color':'ciel','oldPrice': None,'percent': 50,'stock':random.randint(0,10)},
                    {'color':'bleu','oldPrice': None,'percent': 50,'stock':random.randint(0,10)},
                ]
            },
            {
                'L': [
                    {'color':'ciel','oldPrice': None,'percent': 50,'stock':random.randint(0,10)},
                    {'color':'bleu','oldPrice': None,'percent': 50,'stock':random.randint(0,10)},
                ]
            },
        ],
        'tags': ['Coton', 'Laine', 'Monogram'],
        'badge': None,
        'brand': 'Lucas',
        'price': 120,
        'stock': 10,
        'warranty': None,
        'description': 'Dynamique Hawai lunaire chemise de classe moderne',
        'imgDefault': 'images/shirt-14.png',
        'imgHover': 'images/shirt-17.png',
        # shirt-18
    },
    {
        'title': 'Dynamique Hawai',
        'category': 'Chemise',
        'colors': ['ciel', 'bleu'],
        'sizes': [
            {
                'S': [
                    {'color':'ciel','oldPrice': None,'percent': 35,'stock':random.randint(0,10)},
                    {'color':'bleu','oldPrice': None,'percent': 35,'stock':random.randint(0,10)},
                ]
            },
            {
                'M': [
                    {'color':'ciel','oldPrice': None,'percent': 35,'stock':random.randint(0,10)},
                    {'color':'bleu','oldPrice': None,'percent': 35,'stock':random.randint(0,10)},
                ]
            },
            {
                'L': [
                    {'color':'ciel','oldPrice': None,'percent': 35,'stock':random.randint(0,10)},
                    {'color':'bleu','oldPrice': None,'percent': 35,'stock':random.randint(0,10)},
                ]
            },
        ],
        'tags': ['Coton', 'Laine', 'Monogram'],
        'badge': None,
        'brand': 'Lucas',
        'price': 120,
        'warranty': None,
        'description': 'Dynamique Hawai lunaire chemise de classe moderne',
        'imgDefault': 'images/shirt-14.png',
        'imgHover': 'images/shirt-17.png',
    },
    {
        'title': 'Red shirt lunaire',
        'category': 'Chemise',
        'sizes': [
            {
                'S': [
                    {'color':'rouge','oldPrice': None,'percent': 20,'stock':random.randint(0,10)},
                ]
            },
            {
                'M': [
                    {'color':'rouge','oldPrice': None,'percent': 20,'stock':random.randint(0,10)},
                ]
            },
            {
                'L': [
                    {'color':'rouge','oldPrice': None,'percent': 20,'stock':random.randint(0,10)},
                ]
            },
            {
                'XL': [
                    {'color':'rouge','oldPrice': None,'percent': 20,'stock':random.randint(0,10)},
                ]
            },
        ],
        'tags': ['Coton', 'Laine', 'Textile'],
        'badge': None,
        'brand': 'Marc Antoine',
        'price': 120,
        'warranty': None,
        'description': 'Red shirt lunaire modèle de luxe à la modernité',
        'imgDefault': 'images/shirt-19.png',
        'imgHover': 'images/shirt-20.png',
    },
    {
        'title': 'Carrousel red and black',
        'category': 'Chemise',
        'sizes': [
            {
              'XS': [
                  {'color':'rouge','oldPrice': None,'percent': 30,'stock':random.randint(0,20)},
                  {'color':'gris','oldPrice': None,'percent': 30,'stock':random.randint(0,30)},
              ]
            },
            {
              'S': [
                  {'color':'rouge','oldPrice': None,'percent': 30,'stock':random.randint(0,10)},
                  {'color':'gris','oldPrice': None,'percent': 30,'stock':random.randint(0,10)},
              ]
            },
            {
              'M': [
                  {'color':'rouge','oldPrice': None,'percent': 30,'stock':random.randint(0,10)},
              ]
            },
            {
              'L': [
                    {'color':'rouge','oldPrice': None,'percent': 30,'stock':random.randint(0,10)},
                    {'color':'gris','oldPrice': None,'percent': 30,'stock':random.randint(0,10)},
              ]
            },
        ],
        'tags': ['Coton', 'Rubber', 'Textile'],
        'badge': 'Promotion',
        'brand': 'Stella McCartney',
        'price': 130,
        'warranty': None,
        'description': 'Carrousel red and black moderne et lutece de la modernité',
        'imgDefault': 'images/shirt-21.png',
        'imgHover': 'images/shirt-22.png',
    },
    {
        'title': 'Pull  purple cold',
        'category': 'Chemise',
        'colors': ['violet'],
        'sizes': [
            {
              'S':[
                  {'color':'rouge','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
                  {'color':'violet','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
              ]
            },
            {
              'M':[
                  {'color':'rouge','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
                  {'color':'violet','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
              ]
            },
            {
              'L':[
                  {'color':'rouge','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
                  {'color':'violet','oldPrice': None,'percent': 20,'stock':random.randint(0,20)},
              ]
            },
        ],
        'tags': ['Coton', 'Rubber', 'Textile'],
        'badge': 'Edition',
        'brand': 'Ralph Lauren',
        'price': 120,
        'warranty': None,
        'description': 'Pull  purple cold mordenité du style de classe',
        'imgDefault': 'images/sweater-8.png',
        'imgHover': 'images/sweater-9.png',
    },
    {
        'title': 'Design luck',
        'category': 'T-shirt',
        'sizes': [
            {
                'S': [
                    {'color':'bleu','oldPrice': None,'percent': 5,'stock':random.randint(0,20)},
                    {'color':'noir','oldPrice': None,'percent': 5,'stock':random.randint(0,20)},
                ]
            },
            {
                'M': [
                    {'color':'bleu','oldPrice': None,'percent': 5,'stock':random.randint(0,20)},
                    {'color':'noir','oldPrice': None,'percent': 5,'stock':random.randint(0,20)},
                ]
            },
            {
                'L': [
                    {'color':'bleu','oldPrice': None,'percent': 5,'stock':random.randint(0,20)},
                    {'color':'noir','oldPrice': None,'percent': 5,'stock':random.randint(0,20)},
                ]
            },
        ],
        'tags': ['Coton', 'Rubber', 'Textile'],
        'badge': 'Edition',
        'brand': 'Ralph Lauren',
        'price': 90,
        'warranty': None,
        'description': 'Design luck classe de modernité de luxe',
        'imgDefault': 'images/t-shirt-17.png',
        'imgHover': 'images/t-shirt-18.png',
    },
    {
        'title': 'Sum look floor',
        'category': 'T-shirt',
        'sizes': [
            {
                'S': [
                    {'color':'or','oldPrice': None,'percent': None,'stock':random.randint(0,20)},
                ]
            },
            {
                'M': [
                    {'color':'or','oldPrice': None,'percent': None,'stock':random.randint(0,20)},
                ]
            },
        ],
        'tags': ['Textile', 'Coton', 'Laine'],
        'badge': 'Collection',
        'brand': 'Ralph Lauren',
        'price': 140,
        'warranty': None,
        'description': 'Sum look floor t-shirt en coton de luxe et matériaux composite',
        'imgDefault': 'images/t-shirt-15.png',
        'imgHover': 'images/t-shirt-16.png',
    },
    {
        'title': 'Pull black lucas',
        'category': 'Pull',
        'colors': ['noir','blanc','rouge'],
        'sizes': [
            {
                'S':[
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                    {'color': 'rouge', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'M':[
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                    {'color': 'rouge', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'L':[
                    {'color': 'noir', 'oldPrice': None, 'percent': None, 'stock': random.randint(0, 20)},
                ]
            },
        ],
        'tags': ['Textile', 'Coton', 'Laine'],
        'badge': 'Promotion',
        'brand': 'Flamer',
        'price': 140,
        'warranty': None,
        'description': 'Pull black luca en coton de luxe et matériaux composite',
        'imgDefault': 'images/pull-8.png',
        'imgHover': 'images/pull-7.png',
    },
    {
        'title': 'Clair montègne',
        'category': 'Pull',
        'sizes': [
            {
                'S': [
                    {'color': 'bleu', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'M': [
                    {'color': 'bleu', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 20)},
                ]
            },
            {
                'L': [
                    {'color': 'noir', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 20)},
                    {'color': 'bleu', 'oldPrice': None, 'percent': 20, 'stock': random.randint(0, 20)},
                ]
            },
        ],
        'tags': ['Textile', 'Coton', 'Laine'],
        'badge': 'Promotion',
        'brand': 'Tommy Hilfiger',
        'price': 120,
        'warranty': None,
        'description': 'Clair montègne moderne de luxe et clair voyance',
        'imgDefault': 'images/shirt-10.png',
        'imgHover': 'images/shirt-24.png',
    },
]

list_imageHover = []
list_imageDefault = []

for image in listProducts:
    list_imageHover.append(image["imgDefault"])
    list_imageDefault.append(image["imgHover"])

def test_populate():
    for product_data in listProducts:
        for sizeList in product_data['sizes']:
           print(sizeList)


# populate category
def populate_category_table():

    for item in list_category:
        Category.objects.create(
            name=item['name'],
            thumbnail=item['image']
        )
    print('Category completed !')

# populate size
def populate_size_table():
    for size in list_size:
        if size:
            Size.objects.create(
                code=size
            )
    print('Size completed !')

# populate color
def populate_color_table():
    for color in list_color:
        if color['name']:
            Color.objects.create(
                name=color['name'],
                color=color['hex']
            )
    print('Color completed !')

# populate badge
def populate_badge_table():
    for badge in list_badge:
        if badge['name']:
            Badge.objects.create(
                name=badge['name'],
                className=badge['className']
            )
    print('Badge completed !')

# populate tag
def populate_tag_table():
    for tag in list_tag:
        if tag['name']:
            Tag.objects.create(
                name=tag['name']
            )
    print('Tag completed !')


def populate_product_table():
    i = 0
    for product_data in listProducts:
        try:
            i+=1
            print(i)
            category = Category.objects.get(name=product_data['category'])
            badge = None

            if product_data['badge']:
                badge = Badge.objects.get(name=product_data['badge'])

            product = Product.objects.create(
                title=product_data['title'],
                category=category,
                badge=badge,
                brand=product_data['brand'],
                price=product_data['price'],
                warranty=product_data['warranty'],
                description=product_data['description'],
                imgDefault=product_data['imgDefault'],
                imgHover=product_data['imgHover']
            )
            
            # register tags product
            if product_data['tags']:
                for tag_name in product_data['tags']:
                    tag_obj, _ = Tag.objects.get_or_create(name=tag_name)
                    product.tag.add(tag_obj)
            print(i,product_data['title'])
            # register product Item
            if product_data['sizes']:
                for size_list in product_data['sizes']:
                    for key,items in size_list.items():
                        size_obj = Size.objects.get(code=key)

                        for size in items:
                            color_name = size['color']

                            try:
                                color_obj = Color.objects.get(name=color_name)
                                ProductItem.objects.create(
                                    product=product,
                                    size=size_obj,
                                    color=color_obj,
                                    stock=size['stock'],
                                    percent=size.get('percent'),
                                    oldPrice=size.get('oldPrice'),
                                )
                            except Exception as e:
                                print(e)

        except Exception as e:
            print(e)


def populate_personal_product(nbre):
    for _ in range(nbre):
        category = Category.objects.get(name=random.choice(list_category)['name'])
        badge = random.choice(list_badge)
        badgeValue = None
        if badge['name']:
            badgeValue = Badge.objects.get(name=badge['name'])

        product = Product.objects.create(
            title=faker.sentence(nb_words=3).replace('.', ''),
            category=category,
            badge=badgeValue,
            brand=faker.company(),
           # percent=random.choice([None, 15, 20, 25, 30, 40, 45, 50]),
           # stock=random.randint(5, 50),
            price=random.randint(50, 2500),
            warranty=random.randint(1, 3),
            description=faker.text(max_nb_chars=200),
            imgDefault=random.choice(list_imageDefault),
            imgHover=random.choice(list_imageHover)
        )
        tags = random.sample(list_tag, k=min(3,len(list_tag)))

        for tag in tags:
            if tag['name']:
                tagValue = Tag.objects.get(name=tag['name'])
                product.tag.add(tagValue)

        sizes = random.sample(list_size, k=min(4,len(list_size)))
        sizeValue = None
        colorValue = None
        for size in sizes:
            if size:
                sizeValue = Size.objects.get(code=size)            
            colors = random.sample([c for c in list_color if c['name']],
                               k=min(3, len([c for c in list_color if c['name']])))
            for color in colors:
                if color['name']:
                    colorValue = Color.objects.get(name=color['name'])
                ProductItem.objects.get_or_create(
                    product=product,
                    size=sizeValue,
                    color=colorValue,
                    stock= random.randint(5, 50),
                    percent= random.choice([None, 15, 20, 25, 30, 40, 45, 50])
                    
                )
        print("Produit crée : ", product.title)


if __name__ == '__main__':

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
    print('product faker')
    populate_personal_product(nbre)
    print('Remplissage de produits personalisé')
    populate_product_table()
    print('Base de données remplie avec succès !')




