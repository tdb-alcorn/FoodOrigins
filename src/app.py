from ingredients import get_ingredients
from barcodes import get_country
from origins import origins_us_list
from map_origins import map_origins
import web
import os


urls = (
  '/', 'BarcodeServer',
)

render = web.template.render('static/')

HOST = os.getenv('VCAP_APP_HOST', 'localhost')
PORT = int(os.getenv('VCAP_APP_PORT', 8000))


def main(barcode, num_countries=10):
    country = get_country(barcode)
    r = get_ingredients(barcode)
    if country == 'USA':
        origins = origins_us_list(r['ingredients'])
        if len(origins) > 0:
            origins.sort(ascending=False)
            origins = origins.iloc[:num_countries]
            origins = (origins/origins.sum())
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
        if product != 'NOT_FOUND':
            map_origins(origins)
            with open('./static/map.html', 'r') as r:
                html = r.read()
                one, two = html.split('<body>', 1)
                one = '$def with (product)\n\n' + one
                two = '<h1>$product</h1><br/>\n' + two
                html_new = '<body>'.join([one, two])
            with open('./static/map.html', 'w') as w:
                w.write(html_new)
            return render.map(product=product)
        else:
            return render.index(origins=origins, product=product)


if __name__ == "__main__":
    web.httpserver.runsimple(app.wsgifunc(), (HOST, PORT))
    # map_origins(main('076840100477'))
