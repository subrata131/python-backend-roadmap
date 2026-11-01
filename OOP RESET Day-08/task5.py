class a:
    def show(self):
        print("Class A")

class b:
    def show(self):
        print("Class B")

class c(a,b):
    def show(self):
        print("Class C")   
        super().show()

c1=c()
c1.show()
    
