# GB, 7th, Hangman

import random

with open('stats.txt', "r") as file:
    stats = file.read().split(",")

with open("words.txt", "r") as file:
    content = file.read().split(",")

word = random.choice(content)

print("Loading word list from words.txt...")

print(f"Loading stats from stats.txt... ({stats})")

print(f"Word: {len(word[0:3])}")

print("Guessed letters: (none yet)")

wrong_guesses = 6

guessed_letters = ""


def hangman(wrong_guesses):


# def characters(word, guessed_letters):
    
    display_word = ""

    for letter in word:
        if letter is in word:
            display_word += guessed_letters
        else:
            display_word += "_"

    return display_word


guess = input("Guess a letter:").strip()

# create a list of 10 words on a seperate txt file
# create another file holes win/loss counts. holds two numbers how many wins and losses
# read your files
# use split(",") on the content of the words txt document to create your list of words
# pull win and lose totals from the other txt file and save them as 2 seperate variables
# build the hangman game
# save the correct word as a variable random.choice(name of the list)
# number of wrong guesses
# what letters have been guessed 
# function to display the hangman (needs number of wrong guesses)

# """
# _______
# |     |
# |     O
# |    /|\.
# |    / \.
# |_______
# """
# function to show the letters and spaces (the correct word, letters that have been guessed)
# variable for display word (starts as an empty string)
# loop over the correct word
    # check if letter has been guessed
        # then add letter to the display variable
    # if they haven't guessed the letter
        # add an underscore to the display word
# return the finished display word (outside of the loop)

# main game loop (while True)
    # call function to show hangman
    # print function call to show display word
    # create variable and ask user to guess a letter
    # add the letter to a list of guessed letters
    # check if not letter in word:
        # increase incorrect guesses
    # check if display word is same as the word 
        # tell user they won!!
        # increase win total
        # ask if they wanna play again
            # reset random word, reset wrong guess count
        # If not
        # break out of loop
        # write your wins and losses in ur txt file
# check to see if they lost (if they have 6 wrong guesses)
    # tell them they lost and they suck and theyre a loser
    # tell them what the word is
    # increase the lose count
    # ask if they want to play again

