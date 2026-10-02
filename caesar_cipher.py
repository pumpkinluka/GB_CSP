# GB, 7th, Caesar Cipher

while True:
    output = input("Would you like to (E)ncrypt or (D)ecrypt a message?: ").strip().capitalize()
    if output in ["E","D"]:
        break
    else:
        print("Please enter E or D")

message = input("Enter your message: ").strip()

while True:
    shift = int(input("Enter a shift amount: ").strip())
    if shift >= 0 and shift <=26:
        break
    else:
        print("i'm not a python pro. :c")
        print("Enter a shift amount between 0-26.")

def caesar_shift(message, shift):
   
    result = ""

    for character in message:
        if character .isupper():
            character = ord(character)
            character += shift
            if character > 90:
                character = character - 26
            character = chr(character)
            result += character
        elif character .islower():
            character = ord(character)
            character += shift
            if character > 122:
                character -= 26
            character = chr(character)
            result += character
        else:
            result += character
                            
    return result

if output == "E":
    answer = caesar_shift(message, shift)
    print(f"Your encrypted message is: {answer}")
elif output == "D":
    answer = caesar_shift(message, -shift)
    print(f"Your decrypted message is: {answer}")
