class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)

p1=person("Subrata Das",45)
p1.show()
