# GB, 7th, Hangman

# Player is given 6 wrong guesses

import random

print("Loading word list from words.txt...")

try:
    with open('stats.txt', "r") as file:
        stats = file.read().split(",")
        wins = int(stats[0])
        losses = int(stats[1])
        print(f"Loading stats from stats.txt... (Wins: {wins}, Losses: {losses})")
except:
    wins = 0
    losses = 0

with open("words.txt", "r") as file:
    content = file.read().split(",")


def stage(wrong_guesses):
    hangman = """
    _______
    |     |
    |     
    |    
    |    
    |_______
    """

    if wrong_guesses == 1:
        hangman = """
    _______
    |     |
    |     O
    |    
    |   
    |_______
            """
    elif wrong_guesses == 2:
        hangman = """
    _______
    |     |
    |     O
    |     |
    |    
    |_______
            """
    elif wrong_guesses == 3:
        hangman = """
    _______
    |     |
    |     O
    |    /|
    |    
    |_______
            """
    elif wrong_guesses == 4:
        hangman = """
    _______
    |     |
    |     O
    |    /|\\
    |    
    |_______
            """
    elif wrong_guesses == 5:
        hangman = """
    _______
    |     |
    |     O
    |    /|\\
    |    / 
    |_______
            """
    elif wrong_guesses == 6:
        hangman = """
    _______
    |     |
    |     O
    |    /|\\
    |    / \\
    |_______
            """
    
    return hangman


def characters(word, guessed_letters):
    
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    return display_word


while True:
    word = random.choice(content).upper()
    wrong_guesses = 0
    guessed_letters = []
    while True:
        show = stage(wrong_guesses)
        print(show)
        display = characters(word, guessed_letters)
        print(f"Word: {display}")

        fancy_guess = ""

        for letter in guessed_letters:
            if fancy_guess != "":
                fancy_guess += ", "
            fancy_guess += letter

        print(f"Guessed letters: {fancy_guess}")
        print(f"Wrong guesses: {wrong_guesses}")
        guess = input("Guess a letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly ONE. LETTER.")
        else:
            if guess in guessed_letters:
                print(f"You already guessed {guess}!")
            else:
                guessed_letters.append(guess)

                if guess in word:
                    print(f"Hehe, {guess} is in the word!")
                elif guess not in word:
                    wrong_guesses += 1
                    print(f"{guess} is not in the word! Try again.")

        display = characters(word, guessed_letters)

        if display == word:
            wins += 1
            print(f"Congrats! You guessed the word: {word}")
            
            break
    
        if wrong_guesses == 6:
            print("Aww, you lost! :c loser")
            print(f"The word was: {word}")
            losses += 1
            break

    print(f"Updated stats -- Wins: {wins}, Losses: {losses}")

    again = input("Do you wish to play again?(Y/N): ").strip().upper()
    if again in ['Y']:
        print("Here we go once again!")
    elif again in ['N']:
        print("Ok, thanks for playing!")
        break
    else:
        print("Y = Yes, N = No, incase you needed help there.")

with open('stats.txt', "w") as file:
    file.write(f"{wins}, {losses}")
