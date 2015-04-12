import pandas as pd


df = pd.read_csv('./data/countries_chemicals.csv')
dfg = df.groupby('country')['chemical'].apply(lambda x: list(x))


def get_chemicals(country):
    if country in dfg.index:
        return dfg[country]
    else:
        print "Country %s not found" % country
    return []
