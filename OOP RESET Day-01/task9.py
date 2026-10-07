class bank:
    def __init__(self,n,b):
        self.name=n
        self.__balance=b


    def display(self):
        print("Name:",self.name)
        print("balance:",self.__balance)

b1=bank("subrata",10000)
b1.display()
b1.__balance=5000
b1.display()

