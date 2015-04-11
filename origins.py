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
    comm = process.extractOne(ingredient, commodities)[0]
    return (df[comm[0]] / df[comm[0]].sum()).to_dict()


def origins_us_list(ingredients):
    return [origins_us(ingred) for ingred in ingredients]
