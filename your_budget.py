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

print(f"Your rent is ${rent:.2f} and that is {int(rent/income*100)}% of your income.")
print(f"Your utilities is ${util:.2f} and that is {int(util/income*100)}% of your income.")
print(f"Your groceries is ${groceries:.2f} and that is {int(groceries/income*100)}% of your income.")
print(f"Your transportation is ${transport:.2f} and that is {int(transport/income*100)}%")


print(f"You should save ${income/10} and that is 10% of your income")
print(f"You have  of spending money each month ")

# rent/income*100

# f"${rent:.2f}"