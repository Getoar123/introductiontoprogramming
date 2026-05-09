import csv

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

# Write results to a new CSV file
with open("language_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Header row
    writer.writerow(["language", "count"])

    # Data rows
    for language in counts:
        writer.writerow([language, counts[language]])
