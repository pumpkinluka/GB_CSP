# GB, 7th, Number Information

for number in range(1,21):

    word = "odd"
    div = "divisible by 5"

    if number % 2 == 0:
        word = "even"
        while number / 5:
            print(f"{number} is {word} and {div}")
            break
        else: 
            div = "not divisible by 5"
            print(f"{number} is {word} and {div}")
            break



    else:
        while number / 5:
            print(f"{number} is {word} and {div}")
            break
        else:
            div = "not divisible by 5"
            print(f"{number} is {word} and {div}")
            break




        