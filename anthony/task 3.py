class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Adds money to the balance."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deducts money if balance is sufficient."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw ${amount}. New balance is ${self.balance}.")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        """Displays the account balance."""
        print(f"The balance for account {self.account_number} is ${self.balance}.")

# Create a BankAccount instance
account = BankAccount(account_number="123456789", owner="Anthony")

# Perform some transactions
account.deposit(10000)
account.withdraw(3000)
account.display_balance()