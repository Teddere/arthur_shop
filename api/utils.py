import uuid
import math


def generate_ref():
    code = str(uuid.uuid4()).replace('-','').upper()[10]
    return code

def discount_val(valeur,percent:int):
    return valeur * (percent / 100)

def check_stock(article,quantity):
    if article >= quantity:
        article -= quantity
    else:
        raise ValueError("Stock insuffisant !")