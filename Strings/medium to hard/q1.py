# 1
text = "PythonProgramming"
print("1.", text[6:])

# 2
s = "Hello, Python, Hello, World"
print("2.", s.count("Hello"))

# 3
word = "Development"
rev = ""
for ch in word:
    rev = ch + rev
print("3.", rev)

# 4
sentence = "Python is awesome"
if "Python" in sentence:
    sentence = sentence.replace("awesome", "powerful")
print("4.", sentence)

# 5
text2 = "aaabbbcccaaa"
count = 0
pattern = "aaa"
for i in range(len(text2) - len(pattern) + 1):
    if text2[i:i+3] == pattern:
        count += 1
print("5.", count)

# 6
email = "username@example.com"
username, domain = email.split("@")
print("6. Username:", username)
print("   Domain:", domain)

# 7
line = "The price is 1500 rupees"
number = ""
for ch in line:
    if ch.isdigit():
        number += ch
print("7.", number)

# 8
words = "python-is-simple-and-powerful"
print("8.", " ".join(words.split("-")))

# 9
text3 = "Hello123World45Python"
letters_only = ""
for ch in text3:
    if ch.isalpha():
        letters_only += ch
print("9.", letters_only)

# 10
text4 = "Mississippi"
seen = set()
duplicate = None
for ch in text4:
    if ch in seen:
        duplicate = ch
        break
    seen.add(ch)

print("10.", duplicate)