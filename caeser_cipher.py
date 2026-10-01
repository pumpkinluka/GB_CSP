# GB. Caeser Cipher

while True:
    output = input("Would you like to (E)ncrypt or (D)ecrypt a message?: ").strip().capitalize()
    if output .isnumeric():
        print("wheres my letter")
    else:
        print("please enter e or d")


message = input("Enter your message: ").strip()
shift = float(input("Enter a shift amount: ").strip())

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

if output == "D":
    decrypt = user_output("decrypted")
elif output == "E":
    encrypt = user_output("encrypted")






#for character in message:
    #if message .isletter():

