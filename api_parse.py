import json

api = '''
{
 "user":{"name":"Nurali","location":{"city":"Pitnak"}},
 "orders":[{"product":"Laptop"}]
}
'''

data = json.loads(api)

print(data["user"]["location"]["city"])
print(data["orders"][0]["product"])
