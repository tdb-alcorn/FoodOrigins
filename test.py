import requests

BASE_URL = "http://api.foodessentials.com/"
DEFAULT_PARAMS = {'appid': 'h3hw38z6ucxzy67rbjpyk8jy',
                  'f': 'json'}
SESSION_ID = _tomsession()


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


def createsession(user_id, device_id):
    params = DEFAULT_PARAMS.copy()
    params['uid'] = user_id
    params['devid'] = device_id
    return get('createsession', params).json()['session_id']


def get_ingredients(barcode):
    r = label(SESSION_ID, barcode)
    return r.json()
