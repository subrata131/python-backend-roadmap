class upi:
    def pay(self,a):
        return (f"Paid {a} using upi")

class card:
    def pay(self,a):
        return (f"Paid {a} using card")

u1=upi()
c1=card()
payments=[u1,c1]

for i in payments:
    print(i.pay(500))
