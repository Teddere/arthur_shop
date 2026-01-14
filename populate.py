import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arthur.settings')
import django
django.setup()
from api.models import Product,Category,Size,Color,Badge
