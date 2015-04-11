import pandas as pd


df = pd.read_csv('./data/barcode_country_numbers.csv')
df['nums'] = df['nums'].astype(str)
df['nums'] = df['nums'].apply(lambda n: '0'+n if len(n) < 2 else n)
df.index = df['nums']
dff = dff['country']


def get(barcode_prefix):
    """Barcode prefix must be a string of 2-3 digits."""
    if barcode_prefix in df.index:
        return df[barcode_prefix]
    else:
        # print 'Barcode prefix %s not found' % barcode_prefix
        return 'Unknown'


def get_country(barcode):
    if len(barcode) == 12:
        return get("0"+barcode[0])
    elif len(barcode) == 13:
        country = get(barcode[:3])
        if country == 'Unknown':
            country = get(barcode[:2])
        return country
