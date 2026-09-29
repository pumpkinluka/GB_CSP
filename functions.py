# GB, Functions Notes

# makes code easier to read
# breaks porblems in smaller pieces
# used for repetitive code

def stupid_proof(money):
    while True:
        try:
            amount = float(input(f"What is your monthly {money}: "))
            return amount 
        except:
            print("idiot that is not a number :c")

# Write all your variables
income = stupid_proof("income")
rent = stupid_proof("rent")
util = stupid_proof('utilities')
groceries = stupid_proof("groceries")
transport = stupid_proof("transportation")
savings = income/10

# Write any function you are using 
def calc_percent(income, bill):
    return round(bill/income*100)

# Outputs for the user
print(f"Your rent is ${rent:.2f} that is {calc_percent(income, rent)}% of your income.")
print(f"Your utilities is ${util:.2f} that is {calc_percent(income, util)}% of your income.")
print(f"Your groceries is ${groceries:.2f} that is {calc_percent(income, groceries)}% of your income.")
print(f"Your transportation is ${transport:.2f} that is {calc_percent(income, transport)}% of your income.")
print(f"You should save ${savings:.2f}, that is {calc_percent(income, savings)}% of your income.")
print(f"You have ${income-rent-util-groceries-transport-savings:.2f} left to spend!")