class a:
    def show(self):
        print("Class A")

class b(a):
    def show(self):
        print("Class B")
        super().show()

class c(b):
    def show(self):
        print("Class C")
        super().show()


c1=c()
c1.show()   
