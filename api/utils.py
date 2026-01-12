from decimal import Decimal
import uuid
import math


def generate_ref():
    code = str(uuid.uuid4()).replace('-','').upper()[10]
    return code

def discount_val(valeur,percent):
    newPrice = valeur * (Decimal('1') - Decimal(str(percent)) / Decimal('100') )
    return newPrice

def check_stock(article,quantity):
    if article >= quantity:
        article -= quantity
    else:
        raise ValueError("Stock insuffisant !")