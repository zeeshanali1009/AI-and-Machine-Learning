# Encapsulation example for security by hiding sensitive data

class Banking:
    def __init__(self, accountnumber, balance):
        self.accountnumber = accountnumber
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited balance: {amount}\nNet Cash: {self.__balance}")

    def get_balance(self):
        return self.__balance

# Creating object
account = Banking(12334455, 200000)

# Performing deposit
account.deposit(10000)

# Getting current balance
print("Current Balance:", account.get_balance())
