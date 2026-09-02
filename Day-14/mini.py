class payment:
    def pay(self):
        print("Processing Payment")

class upi(payment):
    def pay(self):
        print("Paying with UPI")

class cradit(payment):
    def pay(self):
        print("Paying with Credit Card")

class cash(payment):
    def pay(self):
        print("Paying with Cash")

payments=[upi(), cradit(), cash()]

for i in payments:
    i.pay()
