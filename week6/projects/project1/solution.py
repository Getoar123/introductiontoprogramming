# Project 1 — Temperature Converter
# Author: Getoar Sopa
# Branch: getoar-project1

# Step 1 — Get input from the user and convert to float
celsius = float(input("Enter temperature in Celsius: "))

# Step 2 — Apply the formula
fahrenheit = (celsius * 9/5) + 32

# Step 3 — Print the result using an f-string
print(f"{celsius}°C = {fahrenheit}°F")
