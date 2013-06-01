import json
import datetime
import requests

def encode_json(obj):
    return [_my_json_encoder(cc) for cc in obj]


def _my_json_encoder(obj, format="%Y-%m-%d %H:%M:%S"):
    for k, v in obj.items():
        if isinstance(v, dict):
            _my_json_encoder(v, format)
        elif isinstance(v, datetime.datetime):
            obj[k] = v.strftime(format)
    return obj
    
#NEEDS Huge improvement
def get_city_names(lat,lon):
    #for now we let user filled here
    prs={'lat':lat,'lng':lon,'username':'rhok2013'}
    r = requests.get('ttp://api.geonames.org/findNearbyPlaceNameJSON',params=prs);
    json_in = r.json()
    geoname = json_in['geonames'][0]
    return geoname['toponymName']


