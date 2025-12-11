text = input("Enter your resume paragraph:")
words = text.lower().split()
total_words = len(words)
unique_words = set(words)
unique_count = len(unique_words)
word_frequency = {}
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1
most_repeated = max(word_frequency,key=word_frequency.get)


print("\n---RESULT---")
print("Total Words:",total_words)
print("Unique words:",unique_count)
print("Most Repeated word:",most_repeated)

