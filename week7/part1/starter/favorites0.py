# favorites0.py
# Task: Print every student's favourite language using csv.reader

import csv

# Open favorites.csv for reading
with open("favorites.csv", "r") as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Loop over remaining rows and print language column (index 1)
    for row in reader:
        print(row[1])
