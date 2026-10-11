class father:
    def show(self):
        print("Father method")

class mother:
    def show(self):
        print("Mother method")

class child(father,mother):
    pass

c1=child()
c1.show()
print(child.mro())
