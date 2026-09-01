class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def show(self):
        print("Name is:",self.name)
        print("Salary is:",self.salary)

class manager(employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        print("Department is:",self.department)


b=manager("subrata",10000,"math")
b.show()