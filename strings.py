# GB, Strings Notes

# string -> anything saved inside of quotation marks "" ''
    # you can use single or double quotation marks, it's the same thing!

name = input("What is your name: ").strip().capitalize()

age = input('How old are you: ')
print(type(age))

# Concatenation -> puts two strings directly next to each other
print(age+age)

print(name + " " + "LaRose")

sentence = "The quick brown fox jumped over the lazy dog."

print(sentence)
print(sentence.replace("dog", "monkey"))
print(len(name)) # <- gets the length of a string

print(f"Your name is {name} and that is {len(name)} letters long. Your first initial is {name[0]}. I think I will call you {name[0:3]}.") # <- 0 = index number

# f-string = formatted string
    # curly brackets -> {} breaks from string, allows you to write code inside of string
    # f and {} work together

# Computers start counting at 0