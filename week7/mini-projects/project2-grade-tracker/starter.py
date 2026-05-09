import csv

# Tracking variables
scores = []
total_students = 0

highest_score = -1
highest_name = ""

lowest_score = 101
lowest_name = ""

# Grade counters
grades = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "F": 0
}

with open("grades.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["name"]
        score = int(row["score"])

        # store for average
        scores.append(score)
        total_students += 1

        # highest
        if score > highest_score:
            highest_score = score
            highest_name = name

        # lowest
        if score < lowest_score:
            lowest_score = score
            lowest_name = name

        # grade bands
        if score >= 90:
            grades["A"] += 1
        elif score >= 80:
            grades["B"] += 1
        elif score >= 70:
            grades["C"] += 1
        elif score >= 60:
            grades["D"] += 1
        else:
            grades["F"] += 1

# Average
average = sum(scores) / len(scores)

# Output
print("=== Quiz Grade Summary ===")
print(f"Students assessed : {total_students}")
print(f"Average score     : {average:.1f}")
print(f"Highest score     : {highest_score} ({highest_name})")
print(f"Lowest score      : {lowest_score} ({lowest_name})\n")

print("Grade Distribution:")
print(f"  A (90-100) : {grades['A']} students")
print(f"  B (80-89)  : {grades['B']} students")
print(f"  C (70-79)  : {grades['C']} students")
print(f"  D (60-69)  : {grades['D']} students")
print(f"  F ( 0-59)  : {grades['F']} students")
