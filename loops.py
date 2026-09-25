# GB, Loops notes

import random

count = 1 # <- Start point OUTSIDE of the loop

# while loop starts with 'while'
while count <= 10: # <- Stop point, always a boolean statement
    print(count)
    count += 1 # <- increase iterator
    # iterator : keeps track of the number of times you did the thing
    # iteration : the thing you're doing

ducks = 1
goose = random.randint(1,11)

while True:
    if ducks == goose:
        break # <- ends the loop
    print("Duck....")
    ducks += 1 # ducks = ducks + 1
print("GOOSE!!!!")

# Complex Data Type : holds other data in it
siblings = ["Bella", "Liam"] # <- Surround by brackets
    # "jakhdsk" must be valid data type
    # variables seperated by commas
    # a variable can hold more than one piece of information

# Adding to a list 
print(siblings[1])
siblings.append("Alexa") # <- adds the item to the end of the list 
siblings.insert(3,"Ash")
print(siblings)

# Remove from a list
siblings.pop() # <- if no number given pop removes the last item
print(siblings)

# print each item in a list 
for sibling in siblings:
    print(sibling)

# For Loops
for num in range(1,25): # range : builds a list for you
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)