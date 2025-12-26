import json
data = {'id': 101, 'product': 'Laptop', 'price': 55000}
json_str = json.dumps(data)
print(json_str)