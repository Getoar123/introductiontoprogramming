import csv

# Read data
counts = {}
total = 0

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        language = row["language"]

        # Optional improvement: case-insensitive counting
        language = language.strip().capitalize()

        total += 1

        if language in counts:
            counts[language] += 1
        else:
            counts[language] = 1

# Sort by popularity (highest first)
sorted_languages = sorted(counts, key=counts.get, reverse=True)

# Output
print("=== Language Popularity Report ===")

rank = 1
for language in sorted_languages:
    count = counts[language]
    print(f"{rank}. {language:<7} : {count:3} students")
    rank += 1

print(f"\nTotal responses: {total}")
