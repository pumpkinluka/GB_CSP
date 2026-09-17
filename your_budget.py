# GB. Your Budget

while True:
    try: 
        income = float(input("What is your monthly income:"))
        break
    except:
        print("Please enter a valid amount.")

while True:
    try: 
        rent = float(input("What is your monthly rent/mortgage:"))
        break
    except:
        print("Please enter a valid amount.")

while True:
    try: 
        util = float(input("What is your monthly utilities:"))
        break
    except:
        print("Please enter a valid amount.")

while True:
    try: 
        groceries = float(input("What is your monthly groceries:"))
        break
    except:
        print("Please enter a valid amount.")

while True:
    try: 
        transport = float(input("What is your monthly transportation:"))
        break
    except:
        print("Please enter a valid amount.")

print(f"Your rent is ${int(rent:.2f)} and that is {rent/income*100}%")
print(f"Your utilities is {rent} and that is  ")
print(f"Your groceries is {rent} and that is  ")
print(f"Your transportation is {rent} and that is  ")

print(f"Your rent is {rent} and that is  ")
print(f"You have f")

# rent/income*100

# f"${rent:.2f}"