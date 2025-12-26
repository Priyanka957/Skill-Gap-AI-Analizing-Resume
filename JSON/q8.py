import json
users = {'users': [{'id': 1, 'name': 'priyanka'}, {'id': 2, 'name': 'shruthi'}]}
for user in users['users']:
    print(user['name'])