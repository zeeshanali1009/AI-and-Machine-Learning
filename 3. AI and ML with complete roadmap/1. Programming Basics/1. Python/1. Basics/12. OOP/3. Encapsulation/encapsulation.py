# encapsulation is the pillar of the oop in which we capsule the important information together like 
# represent the important information about the particular thing collectively in the form of data member 
# and data methods
# we will be explaining it with an example
# like we will be bundling the information in the form of attributes and methods and hiding the important or inimportant part as well

class Account:
    def __init__(self, balance, accountno):
        self.balance = balance
        self.account_no = accountno
    
    def getbalance(self):
        return self.balance

    def debit(self, amount):
        self.balance = self.balance - amount
        print(f"Debited amount {amount} | Remaining balance {self.getbalance()}")

    def credit(self, amount):
        self.balance = self.balance + amount
        print(f"Credited amount {amount} | Remaining balance {self.getbalance()}")

# Creating object
acc1 = Account(10000, 121212)
acc1.debit(100)
acc1.credit(1000)



