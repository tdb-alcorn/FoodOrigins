import requests

BASE_URL = "http://api.foodessentials.com/"
DEFAULT_PARAMS = {'appid': 'h3hw38z6ucxzy67rbjpyk8jy',
                  'f': 'json'}

def get(method, params):
    r = requests.get(BASE_URL+method, params=params)
    return r

def label(sid, barcode):
    params = DEFAULT_PARAMS.copy()
    params['sid'] = sid
    params['u'] = barcode
    return get('label', params)

def createsession(user_id, device_id, version):
    params = DEFAULT_PARAMS.copy()
    params['uid'] = user_id
    params['devid'] = device_id
    params['v'] = version
    return get('createsession', params)
