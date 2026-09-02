class cradit:
    def pay(self):
        print("paying with cradit card")

class upi:
    def pay(self):
        print("paying with upi")

class cash:
    def pay(self):
        print("paying with cash")

payment=[cradit(),upi(),cash()]

for i in payment:
    i.pay()
