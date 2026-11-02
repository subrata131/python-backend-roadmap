class number:
    def __init__(self,n):
        self.values=n

    def __gt__(self,m):
        return self.values>m.values

n1=number(100)
n2=number(50)
print(n1>n2)
