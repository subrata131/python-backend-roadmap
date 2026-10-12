class upipayment:
    def pay(self,amount):
        print(f"Paid ${amount} using upi")

class cardpayment:
    def pay(self,amount):
        print(f"Paid ${amount} using card")

u1=upipayment()
c1=cardpayment()
payment=[u1,c1]
for i in payment:
    i.pay(500)
