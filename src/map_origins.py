import folium
import pandas as pd


def map_origins(origins):
    countries = '../data/countries_geo.json'
    df = pd.DataFrame(origins[1])
    df['country'] = df.index

    origins_map = folium.Map(location=[48, -102])
    origins_map.geo_json(geo_path=countries, data=df,
                         columns=['country', 'quantity'],
                         key_on='feature.properties.name',
                         fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
                         legend_name='Origins Quantity')
    origins_map.create_map(path='./static/map.html')
