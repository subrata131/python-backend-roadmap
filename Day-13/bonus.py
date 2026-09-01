class account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def show(self):
        print("Owner is:",self.owner)
        print("Balance is:",self.balance)   

class saving(account):

    def calculateinterest(self,rate):
        interest=self.balance*rate/100
        print("Interest is:",interest)



s=saving("subrata",10000)
s.calculateinterest(5)

s.show()