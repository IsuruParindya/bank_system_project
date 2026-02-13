accountNo = input("Enter Account Numbder :")
accountName = input("Enter Customer Name :")
accountType = input("Enter Account Type :")
balance = float(input("Enter Balance :"))

def showAccount():
    print("Account No :{} \nAccount Name : {} \nAccount Type :{} \nBalance : {} ".format(accountNo, accountName, accountType, balance))

def withDraw(balance, amount):
    if accountType == "SAVING":
        newBalance = balance - amount
        if newBalance < 500:  # Check minimum amount
            raise Exception("Insufficient Fund !! Cannot withdaw money")
        else:
            balance = newBalance
            return balance
    elif accountType == "CURRENT":
        balance = balance - amount
        return balance
    else:
        raise Exception("Invalid Option, Please enter SAVING/CURRENT ")

# --- NEW FUNCTION ADDED ---
def deposit(balance, amount):
    if amount <= 0:
        raise Exception("Deposit amount must be positive!")
    balance += amount
    print(f"Deposited: {amount}")
    return balance

# --- Existing flow ---
showAccount()
amount = float(input("Enter Amount to be Withdrawan :"))
balance = withDraw(balance, amount)
print("After withdraw new balance : ")
print("Balance : ", balance)

# --- Optional new flow to deposit ---
deposit_choice = input("Do you want to deposit money? (yes/no): ").lower()
if deposit_choice == "yes":
    dep_amount = float(input("Enter amount to deposit: "))
    balance = deposit(balance, dep_amount)
    print("After deposit new balance : ", balance)
