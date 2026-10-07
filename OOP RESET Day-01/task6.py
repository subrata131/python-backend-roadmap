class student:
    collage="Brainware University"

    def __init__(self,n,r):
        self.name=n
        self.roll=r

    def display(self):
        print("Name:",self.name)
        print("Roll:",self.roll)
        print("Collage:",self.collage)


s1=student("Subrata",101)
s1.display()