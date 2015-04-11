import pandas as pd
from fuzzywuzzy import process


df = pd.read_csv('./data/us_imports_commodity_country.csv')
commodities = set(df['commodity'])
df = df.groupby(['commodity', 'country'])['quantity'].sum()


def origins(destination_country, ingredient):
    '''
    Takes a country and ingredient and returns a dictionary of countries
    and probabilities of origin (fraction of imports).
    '''
    pass


def origins_us(ingredient):
    comm = process.extractOne(ingredient, commodities)
    return df[comm[0]] / df[comm[0]].sum()


def origins_us_list(ingredients):
    origins = [origins_us(ingred) for ingred in ingredients]
    df = reduce(lambda x, y: x.add(y, fill_value=0), origins)
    df = df / df.sum()
    return df
