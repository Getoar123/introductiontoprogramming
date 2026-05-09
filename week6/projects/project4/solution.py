# Project 4 — Word Counter
# Author: Getoar Sopa

sentence = input("Enter a sentence: ")

# Convert to lowercase and split into words
words = sentence.lower().split()

# Count total words
total_words = len(words)

# Count total characters without spaces
total_characters = len(sentence.replace(" ", ""))

# Build word frequency dictionary
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Print results
print(f"Total words: {total_words}")
print(f"Total characters (no spaces): {total_characters}")
print("Word frequency:")

for word, count in frequency.items():
    print(f"  {word} -> {count}")
