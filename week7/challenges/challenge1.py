import csv

# Ask user for minimum count
minimum = int(input("Minimum votes: "))

with open("../week1/favorites.csv", "r") as file:
    reader = csv.DictReader(file)

    counts = {}

    # Count languages
    for row in reader:
        favorite = row["language"]

        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# Filter + print only those meeting threshold
for language in counts:
    if counts[language] >= minimum:
        print(f"{language}: {counts[language]}")
