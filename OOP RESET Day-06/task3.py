from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self,a):
        pass

class upi(payment):
   
    def pay(self,a):
        print(f"Paid {a} using upi")

class card(payment):
    

    def pay(self,a):
        print(f"Paid {a} using card")

u1=upi()
c1=card()
u1.pay(500)
c1.pay(500)

