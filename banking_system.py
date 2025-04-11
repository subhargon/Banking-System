# Simple Banking System 

class Account:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f" Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print(" Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(" Insufficient balance.")
        elif amount <= 0:
            print(" Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f" Withdrawn ${amount:.2f}. New balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f" Current balance: ${self.balance:.2f}")

# Storing accounts using a dictionary 
accounts = {}

def create_account():
    name = input("Enter your name: ")
    pin = input("Choose a 4-digit PIN: ")
    if name in accounts:
        print(" Account with this name already exists.")
    elif len(pin) != 4 or not pin.isdigit():
        print(" PIN must be exactly 4 digits.")
    else:
        accounts[name] = Account(name, pin)
        print(f" Account created for {name}!")

def login():
    name = input("Enter your name: ")
    pin = input("Enter your PIN: ")
    account = accounts.get(name)
    if account and account.pin == pin:
        print(f" Welcome back, {name}!")
        account_menu(account)
    else:
        print(" Invalid name or PIN.")

def account_menu(account):
    while True:
        print("\n--- Account Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            account.check_balance()
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "4":
            print(" Logging out...")
            break
        else:
            print(" Invalid option. Try again.")

def main():
    while True:
        print("\n=== Welcome to Simple Bank ===")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print(" Thank you for trusting our Bank. Have a nice day!")
            break
        else:
            print(" Invalid option. Try again.")

main()

