import json
import datetime

class MyJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return datetime.strptime(obj, '%Y-%m-%d %H:%M:%S')
        return json.JSONEncoder.default(self,obj)