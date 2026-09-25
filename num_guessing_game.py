# GB. 7th. Number Guessing Game

import random

print("Ready to play? I'm thinking of a number between 1 and 100. You have 5 tries to guess it!")

number = random.randint(1,101)
guess = input("Guess #1: ")
tries = 0
low = print("Too low!")
high = print("Too high!")

while True:
    if number == guess:
        tries += 1
        print(f"Correct! You guessed it in {tries} tries!")
        break
    elif guess > number:
        tries += 1
        print(high)
    elif guess < number:
        tries += 1
        print(low)

if tries == 5:
    print(f"Too bad... you're out of guesses! The number was {number}.")