from ingredients import get_ingredients
from barcodes import get_country
from origins import origins_us_list
import web
import os


urls = (
  '/', 'BarcodeServer'
)

render = web.template.render('static/')

PORT = int(os.getenv('VCAP_APP_PORT', 8000))


def main(barcode, num_countries=10):
    country = get_country(barcode)
    r = get_ingredients(barcode)
    if country == 'USA':
        origins = origins_us_list(r['ingredients'])
        if len(origins) > 0:
            origins.sort(ascending=False)
            origins = origins.iloc[:num_countries]
            origins = (origins/origins.sum()).to_dict()
    else:
        origins = {}
    return r['product_name'], origins


app = web.application(urls, globals())

class BarcodeServer:
    def GET(self):
        return render.form()

    def POST(self):
        form = web.input(barcode="")
        product, origins = main(form.barcode)
        return render.index(origins=origins, product=product)

if __name__ == "__main__":
    app.run(port=PORT)
