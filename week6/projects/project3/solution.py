# Project 3 — Grade Calculator
# Author: Getoar Sopa

scores = []

for i in range(5):
    score = float(input(f"Enter score {i + 1}: "))
    scores.append(score)

# Calculate average
average = sum(scores) / len(scores)

# Determine grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Print results
print(f"Average: {average}")
print(f"Grade: {grade}")
