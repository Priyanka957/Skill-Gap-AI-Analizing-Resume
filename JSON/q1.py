import json

json_str = '{"name": "priyanka","age": 19, "city": "Hyderabad"}'
python_dict = json.loads(json_str)
print(python_dict)