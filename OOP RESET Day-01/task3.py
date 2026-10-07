class employee:
    def __init__(self,n,s):
        self.name=n
        self.salary=s

    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)

e1=employee("Subrata",20000)
e1.display()
e2=employee("Jadab",250000)
e2.display()