import json
data = {"technical_skills":["python","java"],
        "soft_skills":["teamwork","communication"]}
print(json.dumps(data, indent = 2))