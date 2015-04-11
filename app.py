import ingredients
from barcodes import get_country


def main(barcode):
    country = get_country(barcode)
    r = ingredients.get_ingredients(barcode)
