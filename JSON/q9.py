import json
person = {'name': 'priya', 'age': 19}
person['country'] = 'India'
json_str = json.dumps(person)
print(json_str)