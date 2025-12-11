# 1
print("1. Numbers 1 to 10:")
for i in range(1, 11):
    print(i)
print()

# 2
print("2. Even numbers 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
print()

# 3
print("3. Characters in 'Python':")
for ch in "Python":
    print(ch)
print()

# 4
print("4. Numbers 5 to 1:")
i = 5
while i >= 1:
    print(i)
    i -= 1
print()

# 5
print("5. Sum of numbers 1 to 50:")
total = 0
for i in range(1, 51):
    total += i
print(total)
print()

# 6
print("6. Multiplication table of 5:")
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)
print()

# 7
print("7. Vowel count in 'Programming':")
vowels = "aeiou"
count = 0
for ch in "programming":
    if ch in vowels:
        count += 1
print(count)
print()

# 8
print("8. Reverse of 'PythonLoops':")
s = "PythonLoops"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)
print()

# 9
print("9. Skip 5:")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
print()

# 10
print("10. Stop when number reaches 13:")
for i in range(1, 21):
    if i == 13:
        break
    print(i)
print()

# 11
print("11. Prime check for 29:")
num = 29
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
print()

# 12
print("12. Character count in 'mississippi':")
word = "mississippi"
count_dict = {}

for ch in word:
    if ch in count_dict:
        count_dict[ch] += 1
    else:
        count_dict[ch] = 1

print(count_dict)
print()

# 13
print("13. Pattern:")
for i in range(1, 6):
    print("*" * i)
print()

# 14
print("14. Largest digit in 5847361:")
num = "5847361"
largest = max(num)
print(largest)
print()

# 15
print("15. Reverse pattern:")
for i in range(4, 0, -1):
    print("*" * i)