# GB, Vibe Code for a Theater

while True:
    try:
        age = int(input("Enter your age: ").strip())
        if age < 0:
            print("Invalid age")
        else:
            break
    except:
        print("Invalid age")

matinee = input("Is this a matinee? (yes/no): ").lower().strip()

if age < 5:
    price = 0
elif age < 13:
    price = 8
elif age < 65:
    price = 12
else:
    price = 9

if matinee == "yes" and price >= 3:
    price = price - 3

print(f"Ticket price: ${price:.2f}")