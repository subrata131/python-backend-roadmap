class vehicle:
    def __init__(self,b,s):
        self.brand=b
        self.speed=s

    def display(self):
        print("Vehicle Brand:",self.brand)
        print("Vehicle Speed:",self.speed)

class bike(vehicle):
    
    def __init__(self,b,s,t):
        super().__init__(b,s)
        self.helmet_required=t

    def display_bike(self):
        
        super().display()
        print("Helmet Required:", self.helmet_required)

b1 = bike("Honda", 80, True)
b1.display_bike()
b1.display()
