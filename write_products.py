import json

products = [
    {"id":1,"name":"Laptop","price":10000000},
    {"id":2,"name":"Mouse","price":1000000}
]

with open("products.json","w") as f:
    json.dump(products,f,indent=4)
