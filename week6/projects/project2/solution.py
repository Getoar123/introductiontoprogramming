# Project 2 — Number Guessing Game
# Author: Getoar Sopa

import random

# Step 1 — Pick a random number between 1 and 10
secret = random.randint(1, 10)

# Step 2 — Set up a counter
guesses = 0

# Step 3 — Ask the user for their first guess
guess = int(input("Guess a number between 1 and 10: "))

# Step 4 — Loop until the guess is correct
while guess != secret:
    guesses += 1

    if guess < secret:
        guess = int(input("Too low! Try again: "))
    else:
        guess = int(input("Too high! Try again: "))

# Count the correct guess
guesses += 1

print(f"Correct! You got it in {guesses} guesses.")
