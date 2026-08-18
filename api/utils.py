from decimal import Decimal
import uuid
import random
import string


def generate_ref():
    uuid_part = str(uuid.uuid4()).replace('-','').upper()[:8]
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"{uuid_part}{code}"

def discount_val(valeur,percent):
    newPrice = Decimal(valeur) * (Decimal('1') - Decimal(str(percent)) / Decimal('100') )
    return newPrice

def _generate_sku(product,size,color):
    size_code = size.code[:3].upper() if size else 'NS'
    color_code = color.name[:3].upper() if color else 'NC'
    return f'{product.ref}-{size_code}-{color_code}'
def check_stock(article,quantity):
    if article >= quantity:
        article -= quantity
    else:
        raise ValueError("Stock insuffisant !")