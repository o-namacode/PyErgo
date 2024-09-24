from datetime import datetime
from json import JSONEncoder


class PyErgoJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

