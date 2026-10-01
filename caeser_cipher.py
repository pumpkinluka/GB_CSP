# GB. Caeser Cipher

output = input("Would you like to (E)ncrypt or (D)ecrypt a message?: ")
message = input("Enter your message: ")
shift = input("Enter a shift amount: ")


for character in message:
    if character .isalpha():
        character = ord(character)
        character = character + shift
        if character >= 122:
            character = character - 26
        character = chr(character)
    crypt = "encrypted"
    e = "E"
    d = "D"

    if letter .isalpha():
        if output == e:
        print("hey")
        break
    elif output == d:
        crypt = "decrypted"
        break
    elif output .isnumeric():
        print("give me letters ONLY!!")
    else:
        print("E or D, choose one!")

def user_output(kind):
    crypt_msg = print(f"Your {kind} message is: ")
    return crypt_msg


decrypt = user_output("decrypted")
encrypt = user_output("encrypted")






#for character in message:
    #if message .isletter():

