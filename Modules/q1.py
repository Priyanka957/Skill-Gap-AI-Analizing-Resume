import math
import random
import datetime
import os
import sys
import json
import re
import statistics
import time

print("1. Square root of 25 =", math.sqrt(25))

print("2. Floor of 5.67 =", math.floor(5.67))
print("   Ceil of 5.67 =", math.ceil(5.67))

print("3. Random number (1–100) =", random.randint(1, 100))

print("4. Five random integers (10–20):")
for _ in range(5):
    print(random.randint(10, 20))

print("5. Today's date =", datetime.date.today())

today = datetime.date.today()
print("6. Year:", today.year)
print("   Month:", today.month)
print("   Day:", today.day)

print("7. Current working directory:", os.getcwd())

print("8. Files in current directory:", os.listdir())

print("9. Python version:", sys.version)

json_str = '{"name":"Priya","age":20}'
print("10. JSON to dict:", json.loads(json_str))

print("11. cos(0) =", math.cos(0))
print("    sin(90°) =", math.sin(math.radians(90)))
print("    log(10) =", math.log(10))

print("12. Rolling a dice 10 times:")
dice_results = [random.randint(1, 6) for _ in range(10)]
print(dice_results)

birthday = datetime.date(2026,2,16)
days_left = birthday - today
print("13. Days left for next birthday:", days_left.days)

date_str = "2022-05-15"
dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
dt_after_30 = dt + datetime.timedelta(days=30)
print("14. Date after adding 30 days:", dt_after_30.date())

folder_name = "backup"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
print("15. Folder 'backup' created (if not existed).")

data = {"name": "Priya", "age": 20}
json_data = json.dumps(data)
print("16. Dict to JSON:", json_data)

text = "My phone number is 98765"
digits = re.findall(r"\d+", text)
print("17. Extracted digits:", digits)

word = "HelloWorld"
match = re.match(r"Hello", word)
print("18. Starts with Hello? =", bool(match))

numbers = [10, 20, 30, 40, 50]
print("19. Mean =", statistics.mean(numbers))
print("    Median =", statistics.median(numbers))
print("    Mode (dummy example) =", statistics.mode([1, 1, 2, 3]))

start = time.time()
for i in range(1, 1000001):
    pass
end = time.time()
print("20. Loop execution time (1 to 1,000,000):", end - start, "seconds")