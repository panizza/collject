import json
import datetime


def encode_json(obj):
    return [_my_json_encoder(cc) for cc in obj]


def _my_json_encoder(obj, format="%Y-%m-%d %H:%M:%S"):
    for k, v in obj.items():
        if isinstance(v, dict):
            _my_json_encoder(v, format)
        elif isinstance(v, datetime.datetime):
            obj[k] = v.strftime(format)
    return obj

