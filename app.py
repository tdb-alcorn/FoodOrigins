from ingredients import get_ingredients
from barcodes import get_country
from origins import origins_us_list
import web


urls = (
  '/', 'BarcodeServer'
)

render = web.template.render('static/')

def main(barcode, num_countries=10):
    country = get_country(barcode)
    r = get_ingredients(barcode)
    if country == 'USA':
        origins = origins_us_list(r['ingredients'])
        origins.sort(ascending=False)
        origins = origins.iloc[:num_countries].to_dict()
    else:
        origins = {}
    return origins


app = web.application(urls, globals())

class BarcodeServer:
    def GET(self):
        return render.form()

    def POST(self):
        form = web.input(barcode="")
        origins = main(form.barcode)
        return render.index(origins=origins)

if __name__ == "__main__":
    app.run()
