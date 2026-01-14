from decimal import Decimal
import uuid
import random
import string


def generate_ref():
    uuid_part = str(uuid.uuid4()).replace('-','').upper()[:8]
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"{uuid_part}{code}"

def discount_val(valeur,percent):
    newPrice = valeur * (Decimal('1') - Decimal(str(percent)) / Decimal('100') )
    return newPrice

def check_stock(article,quantity):
    if article >= quantity:
        article -= quantity
    else:
        raise ValueError("Stock insuffisant !")