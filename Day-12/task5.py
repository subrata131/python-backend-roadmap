class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def show(self):
        print("Employee Name:",self.name)
        print("Employee salary:",self.salary)

e1=employee("Subrata Das",12000)
e2=employee("Rahul Das",15000)
e1.show()
e2.show()
