class student:
    def __init__(self,n,r,m):
        self.name=n
        self.roll=r
        self.mark=m

    def is_pass(self):
        if self.mark>=40:
            return "Pass"
        else:
            return "Fail"

    def update_mark(self,new):
        self.mark=new
        print("Mark Update to:",new)

    def display(self):
        re=self.is_pass()
        print("Name:",self.name)
        print("Roll:",self.roll)
        print("Mark:",self.mark)
        print("Result:",re)

s1=student("Subrata",101,38)
s1.display()
s1.update_mark(58)
s1.display()
