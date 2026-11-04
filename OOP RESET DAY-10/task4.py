class employee:
    company="Google"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)

    @classmethod
    def change_company(cls,new):
        cls.company=new

    @staticmethod
    def is_valid_salary(salary):
        if salary>0:
            return True
        else:
            return False

e1=employee("Subrata",30000)
e1.display()
employee.change_company("Microsoft")
print("Company name is:",employee.company)

print(employee.is_valid_salary(30000))
print(employee.is_valid_salary(-500))
