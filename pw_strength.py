# GB, Password Strength Checker

while True:
    characters = False
    uppercase = False
    lowercase = False
    number = False
    symbol = False
    rules = 0
    strength = "invalid"
    missing = []
    combined = characters+uppercase+lowercase+number+symbol

    password = input("What is your password:").strip()

    if (len(password)) >= 8:
        characters = True
        rules += 1
    else: 
        missing.append("at least 8 characters")

    if password .isupper():
        uppercase = True
        rules += 1
    else: 
        missing.append("an uppercase letter")

    if password .islower():
        lowercase = True
        rules += 1
    else: 
        missing.append("a lowercase letter")

    if password .isnumeric():
        number = True
        rules += 1
    else: 
        missing.append("a number")

    if password in "!@#$%^&*()_-=+[]{.,<>?:;}":
        symbol = True
        rules += 1
    else: 
        missing.append("a symbol")

    if rules == 5:
        strength = "Strong"
    elif rules <= 4 and rules > 2:
        strength = "Medium"
    elif rules < 3:
        strength = "Weak"

    print(f"At least 8 characters: {characters}")
    print(f"Has an uppercase letter: {uppercase} ")
    print(f"Has a lowercase letter: {lowercase}")
    print(f"Has a number: {number}")
    print(f"Has a symbol: {symbol}")
    print(f"Your password strength is: {strength}")

    if combined:
        print("All good!")
    else:
        print('To make it strong, add: ' + ", ".join(missing))
