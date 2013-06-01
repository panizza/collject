import json
import datetime


def my_json_encoder(obj,format):
	for k,v in obj.items():
		if isinstance(v, dict):
			my_json_encoder(v,format)
		elif isinstance(v, datetime.datetime):
			obj[k] = datetime.strptime(v, format)
	return obj;