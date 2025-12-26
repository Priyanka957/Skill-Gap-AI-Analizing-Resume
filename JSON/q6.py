import json
person = {'name': 'Raj', 'age': 45}
person['age'] = 50
json_str = json.dumps(person)
print(json_str)