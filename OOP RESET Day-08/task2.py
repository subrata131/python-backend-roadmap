class student:
    def __init__(self,n):
        self.name=n

    def borrow(self,l):
        print(f"{self.name} borrowed a book from {l.lib_name} ")


class library:
    def __init__(self,n):
        self.lib_name=n


s1=student("subrata")
c1=library("central library")

s1.borrow(c1)

