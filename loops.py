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

print(siblings[1])