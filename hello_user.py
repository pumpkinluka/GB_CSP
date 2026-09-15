# GB, Hello User

while True:
    name = input("What is your first name?:").strip().title()
    if name .isnumeric():
        print("Are you a robot? Give me letters please.")
    elif " " in name:
        print("I said FIRST name, silly!")
    else:
        break

print(f"Hello, {name}!")

