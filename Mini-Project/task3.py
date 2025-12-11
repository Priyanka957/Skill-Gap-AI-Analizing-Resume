sentence = input("Enter the sentence:")
words = sentence.split()
experience_years = "Not Found"
for word in words:
    if word.isdigit():
        experience_years = word
        break
print("Experience Detected:",experience_years,"Years")
     