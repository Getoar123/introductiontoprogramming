import csv

error_count = 0

with open("messy_data.csv", "r") as infile, open("clean_data.csv", "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    writer = csv.writer(outfile)

    # Write header for cleaned file
    writer.writerow(["name", "language", "problem"])

    for row in reader:
        name = row.get("name")
        language = row.get("language")
        problem = row.get("problem")

        # Check for missing or empty values
        if not name or not language or not problem:
            error_count += 1
            continue

        # Write only clean rows
        writer.writerow([name, language, problem])

print(f"Cleaning complete.")
print(f"Rows with errors skipped: {error_count}")
