import json
from datetime import datetime

class Encoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,datetime):
            return obj.isoformat()
        return super().default(obj)

data = {"date": datetime.now()}
print(json.dumps(data, cls=Encoder))
