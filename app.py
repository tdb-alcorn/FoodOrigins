from ingredients import get_ingredients
from barcodes import get_country
from origins import origins_us_list


def main(barcode):
    country = get_country(barcode)
    r = get_ingredients(barcode)
    if country == 'USA':
        origins = origins_us_list(r['ingredients']).to_dict()
    else:
        origins = {}
    return origins
