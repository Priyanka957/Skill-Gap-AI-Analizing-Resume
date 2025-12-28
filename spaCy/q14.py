text = "Experience in SQL and NoSQL"
words = text.split()

sql_only = [w for w in words if w == "SQL"]
print(sql_only)