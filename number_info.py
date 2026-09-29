# GB, 7th, Number Information

for number in range(1,21):

    word = "odd"
    div = "divisible by 5"

    if number % 2 == 0:
        word = "even"
        if number % 5 == 0:
            print(f"{number} is {word} and {div}")
        else: 
            div = "not divisible by 5"
            print(f"{number} is {word} and {div}")

    else:
        if number % 5 == 0:
            print(f"{number} is {word} and {div}")
        else:
            div = "not divisible by 5"
            print(f"{number} is {word} and {div}")
  