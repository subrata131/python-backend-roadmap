class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        amount = float(input("Enter deposit amount: "))
        self.balance += amount
        print("Amount deposited successfully.")
        print("Current Balance:", self.balance)

    def show(self):
        print("Account Holder:", self.owner)
        print("Balance:", self.balance)



name = input("Enter account holder name: ")
balance = float(input("Enter opening balance: "))

account = BankAccount(name, balance)

while True:
    print("\n=== Bank Account Manager ===")
    print("1. Deposit")
    print("2. Show Balance")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account.deposit()
    elif choice == 2:
        account.show()
    elif choice == 3:
        print("Thank You!")
        break
    else:
        print("Invalid Choice")