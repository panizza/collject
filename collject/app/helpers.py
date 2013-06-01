import json
import datetime
from django.core.serializers.json import DjangoJSONEncoder

class MyJsonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return datetime.strptime(obj, '%Y-%m-%d %H:%M:%S')
        return super(MyJsonEncoder, self).default(obj)