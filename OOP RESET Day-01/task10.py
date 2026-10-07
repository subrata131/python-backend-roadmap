class bank:
    def __init__(self,n,b):
        self.name=n
        self.__balance=b

    def get_balance(self):
        print("Name:",self.name)
        print("balance:",self.__balance)

    def set_balance(self,b):
        self.__balance=b
        print("Balance updated to:",self.__balance)

b1=bank("Subrata",10000)
b1.get_balance()
b1.set_balance(5000)
b1.get_balance()
