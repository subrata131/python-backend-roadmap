class student:
    def __init__(self,n,r,m):
        self.name=n
        self.roll=r
        self.mark=m

    def is_pass(self):
        if self.mark>=40:
            return("Pass")
        else:
            return("Fail")

    def display(self):
        re=self.is_pass()
        print("Name:",self.name)
        print("Roll:",self.roll)
        print("Mark:",self.mark)
        print("Result:",re)

s1=student("Subrata",101,58)
s1.display()
s2=student("jadab",102,30)
s2.display()