# 1
def welcome():
    print("1. Welcome to Python!")

welcome()
print()


# 2
def greet(name):
    print( "2. Hello", name)

greet("Priya")
print()


# 3
def square(n):
    return n * n

print("3. Square of 5 =", square(5))
print()


# 4
def calculator(a, b):
    return a + b, a - b, a * b

s, d, p = calculator(10, 4)
print("4. Sum:", s)
print("Difference:", d)
print("Product:", p)
print()


# 5
def country(name="India"):
    print("5. I am from", name)

country()
print()


# 6
def total(*nums):
    return sum(nums)

print("6. Total =", total(5, 10, 15))
print()


# 7
def student_info(**data):
    for key, value in data.items():
        print("7.",key, ":", value)

student_info(name="Priya", age=20, course="Python")
print()


# 8
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

print("8. Vowels in 'Programming' =", count_vowels("Programming"))
print()


# 9
cube = lambda x: x * x * x
print("9. Cube of 3 =", cube(3))
print()


# 10
def unique_letters(text):
    result = ""
    for ch in text:
        if ch not in result:
            result += ch
    return result

print("10. Unique letters:", unique_letters("mississippi"))