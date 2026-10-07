class student:
    def __init__(self,n,a):
        self.name=n
        self.age=a

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

s1=student("subrata",20)
s1.display()
s2=student("Jadab",18)
s2.display()