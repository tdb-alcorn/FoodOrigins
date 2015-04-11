import requests
import re


BASE_URL = "http://api.foodessentials.com/"
DEFAULT_PARAMS = {'appid': 'h3hw38z6ucxzy67rbjpyk8jy',
                  'f': 'json'}


def createsession(user_id, device_id):
    params = DEFAULT_PARAMS.copy()
    params['uid'] = user_id
    params['devid'] = device_id
    return get('createsession', params).json()['session_id']


def _tomsession():
    return createsession('tom', 'test')


def get(method, params):
    r = requests.get(BASE_URL+method, params=params, data={'api_key': params['appid']})
    return r


def label(sid, barcode):
    params = DEFAULT_PARAMS.copy()
    params['sid'] = sid
    params['u'] = barcode
    return get('label', params)


def parse_ingredients(ingred_list):
    return re.split(',(?=[^\)]*(?:\(|$))', ingred_list)


SESSION_ID = _tomsession()


def get_ingredients(barcode):
    r = label(SESSION_ID, barcode)
    result = r.json()
    result['ingredients'] = parse_ingredients(result['ingredients'])
    out = {}
    for key in result:
        if key in ['ingredients', 'product_name']:
            out[key] = result[key]
    return out
