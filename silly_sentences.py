# GB, 7th, Silly Sentences

while True:
    verb = input("Tell me a verb ending in -ing: ").strip().lower()
    if verb .isnumeric():
        print("Give me a word, not a number.")
    elif " " in verb:
        print("Just one singular word!")
    else:
        break

while True:
    country = input("Tell me a one-word country: ").strip().title()
    if country .isnumeric():
        print("Give me a word, not a number.")
    elif " " in country:
        print("Just one singular word!")
    else:
        break

while True:
    adj = input("Tell me an adjective: ").strip().lower()
    if adj .isnumeric():
        print("Give me a word, not a number.")
    elif " " in adj:
        print("Just one singular word!")
    else:
        break

while True:
    animal = input("Tell me an animal: ").strip().lower()
    if animal .isnumeric():
        print("Give me a word, not a number.")
    elif " " in animal:
        print("Just one singular word!")
    else:
        break

while True:
    food = input("Tell me a food: ").strip().lower()
    if food .isnumeric():
        print("Give me a word, not a number.")
    elif " " in food:
        print("Just one singular word!")
    else:
        break

while True:
    thing = input("Tell me a thing: ").strip().lower()
    if thing .isnumeric():
        print("Give me a word, not a number.")
    elif " " in thing:
        print("Just one singular word!")
    else:
        break

print("I was " + verb + " in " + country + " when I saw a " + adj + " " + animal + " eating " + food + " on a " + thing + ".")