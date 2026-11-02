class number:
    def __init__(self,n):
        self.values=n

    def __mul__(self,m):
        return self.values*m.values

n1=number(10)
n2=number(5)    
print(n1*n2)
