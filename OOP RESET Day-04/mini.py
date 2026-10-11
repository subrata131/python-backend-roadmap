class person:
    def __init__(self,n):
        self.name=n

class student(person):
    def __init__(self,n,r):
        super().__init__(n)
        self.roll=r

class exam(student):
    def __init__(self,n,r,m):
        super().__init__(n,r)
        self.mark=m

    def display(self):
        print("Name:",self.name)
        print("Roll:",self.roll)
        print("Mark:",self.mark)

s1=exam("Subarta",101,85)
s1.display()
print(isinstance(s1,person))
print(isinstance(s1,student))
print(isinstance(s1,exam))


