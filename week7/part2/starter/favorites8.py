import csv

with open("../week1/favorites.csv", "r") as file:
    reader = csv.DictReader(file)

    counts = {}

    for row in reader:
        favorite = row["language"]

        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# Sort by count (highest first)
for language in sorted(counts, key=counts.get, reverse=True):
    print(f"{language}: {counts[language]}")
