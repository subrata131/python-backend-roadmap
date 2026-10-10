class employee:
    def __init__(self,n,s):
        self.name=n
        self.salary=s

class manager(employee):
    def __init__(self,n,s,d):
        super().__init__(n,s)
        self.department=d

    def display_manager(self):
        print("Manager Name:",self.name)
        print("Manager Salary:",self.salary)
        print("Manager Department:",self.department)

m1=manager("John","50000","IT")
m1.display_manager()

