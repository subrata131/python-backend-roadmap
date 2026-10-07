class bank:
    def __init__(self,n,b):
        self.name=n
        self.balance=b

    def deposite(self,a):
        self.balance+=a
        print("Amount deposite:",a)

    def display(self):
        print("Name:",self.name)
        print("Balance:",self.balance)

b1=bank("Subrata",10000)
b1.deposite(5000)
b1.display()