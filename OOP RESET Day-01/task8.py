class bank:
    def __init__(self,n,b):
        self.name=n
        self.balance=b


    def display(self):
        print("Name:",self.name)
        print("balance:",self.balance)

b1=bank("subrata",10000)
b1.display()
b1.balance=5000
b1.display()