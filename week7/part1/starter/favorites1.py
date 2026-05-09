import csv

with open("favorites.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        # Store language in a variable
        favorite = row[1]

        # Print it
        print(favorite)
