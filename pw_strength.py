# GB, 7th, Password Strength Checker

characters = False
uppercase = False
lowercase = False
number = False
symbol = False
score = 0
strength = "Weak"

password = input("What is your password:").strip()

if (len(password)) >= 8:
    characters = True
    score = score + 1

print(f"At least 8 characters: {characters}")


for letter in password:
    if letter.isupper():
        uppercase = True

if uppercase:
    score = score + 1

print(f"Has an uppercase letter: {uppercase} ")
   
for letter in password:
    if letter.islower():
        lowercase = True

if lowercase:
    score = score + 1

print(f"Has a lowercase letter: {lowercase}")
  
for letter in password:
    if letter.isnumeric():
        number = True

if number:
    score = score + 1

print(f"Has a number: {number}")
  
for letter in password:
    if letter in "!@#$%^&*()_-=[+]{.,<>?:;}/~|":
        symbol = True

if symbol:
    score = score + 1

print(f"Has a symbol: {symbol}")


if score == 5:
    strength = "Strong"
elif score <= 4 and score > 2:
    strength = "Medium"
elif score < 3:
        strength = "Weak"

print(f"Your password strength is: {strength}")

if strength != "Strong":
    missing = ""

    if not characters:
        missing = missing + "at least 8 characters"

    if not uppercase:
        if missing != "":
            missing = missing + ", "
        missing = missing + "an uppercase letter"

    if not lowercase:
        if missing != "":
            missing = missing + ", "
        missing = missing + "a lowercase letter"

    if not number:
            if missing != "":
                missing = missing + ", "
            missing = missing + "a number"

    if not symbol:
            if missing != "":
                missing = missing + ", "
            missing = missing + "a symbol"

    print(f"To make it strong, add: {missing}")
    
        
