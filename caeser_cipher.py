# GB. Caeser Cipher

output = input("Would you like to (E)ncrypt or (D)ecrypt a message?: ").strip()
message = input("Enter your message: ").strip()
shift = input("Enter a shift amount: ").strip()

def caeser_shift(message, shift):

    for character in message:
        if character .isalpha():
            character = ord(character)
            character = character + shift
            if character >= 122:
                character = character - 26
            character = chr(character)


def user_output(kind):
    crypt_msg = print(f"Your {kind} message is: ")
    return crypt_msg


decrypt = user_output("decrypted")
encrypt = user_output("encrypted")






#for character in message:
    #if message .isletter():

