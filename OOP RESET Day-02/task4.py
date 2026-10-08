class person:
    def __init__(self,n):
        self.name=n

class student(person):
    def __init__(self,n,r):
        super(). __init__(n)
        self.roll=r

    def display(self):
        print("Name:",self.name)
        print("Roll:",self.roll)
s1=student("Subrata",101)
s1.display()
