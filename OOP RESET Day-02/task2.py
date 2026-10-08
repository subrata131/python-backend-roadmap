class bank:
    def __init__(self,n,b):
        self.name=n
        self.__balance=b

    def deposite(self,a):
        if a>0:
            self.__balance+=a
            print("Amount deposited:",a)
        else:
            print("Invalid amount")

    def withdraw(self,a):
        if a>0 and a<=self.__balance:
            self.__balance-=a
            print("Amount withdrawn:",a)
        else:
            print("Invalid amount or insufficient balance")

    def get_balance(self):
        print("Current balance is:",self.__balance)


b1=bank("subrata",10000)
b1.get_balance
b1.deposite(50000)
b1.get_balance()
b1.withdraw(20000)
b1.get_balance()
b1.withdraw(600000)




    