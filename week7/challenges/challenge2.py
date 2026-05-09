import csv

with open("../week1/favorites.csv", "r") as file:
    reader = csv.DictReader(file)

    # Nested dictionary:
    # { language: { problem: count } }
    data = {}

    for row in reader:
        language = row["language"]
        problem = row["problem"]

        if language not in data:
            data[language] = {}

        if problem in data[language]:
            data[language][problem] += 1
        else:
            data[language][problem] = 1

# Now find most common problem per language
for language in data:
    problems = data[language]

    most_common = None
    highest_count = 0

    for problem in problems:
        if problems[problem] > highest_count:
            highest_count = problems[problem]
            most_common = problem

    print(f"{language}: {most_common}")
