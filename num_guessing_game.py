# GB. 7th. Number Guessing Game

# Secret number is between 1-100
# The player gets 7 attempts

import random

print("Ready to play? I'm thinking of a number between 1 and 100. You have 7 tries to guess it!")

number = random.randint(1,100)
max = 7
guess_num = 1

for tries in range(max):
    guess = int(input(f"Guess #{guess_num}: "))

    if number < guess:
        tries += 1
        guess_num += 1
        print("Too high!")
    elif guess < number:
        tries += 1
        guess_num += 1
        print("Too low!")
    else: 
        tries += 1
        print(f"Correct! You guessed it in {tries} tries!")
        break

if number != guess and tries == 7:
    print(f"Too bad... you're out of guesses! The number was {number}.")