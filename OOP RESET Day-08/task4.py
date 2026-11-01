class grandfather:
    def show(self):
        print("Grandfather Method")

class father:
    def show(self):
        print("Father Method")

class child(grandfather,father):
    pass

c1=child()
c1.show()

print(child.mro())
