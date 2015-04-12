import folium
import pandas as pd


def map_origins(origins):
    countries = './data/countries_geo.json'
    df = pd.DataFrame(origins, columns=['quantity'])
    df['country'] = df.index
    df['quantity'] = df['quantity'] * 100

    origins_map = folium.Map(location=[20, 20], zoom_start=2)
    origins_map.geo_json(geo_path=countries, data=df, data_out='./data/data.json',
                         columns=['country', 'quantity'],
                         key_on='feature.properties.name',
                         fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
                         legend_name='Origins Quantity', reset=True)
    origins_map.create_map(path='./static/map.html')
