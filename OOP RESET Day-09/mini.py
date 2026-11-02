class number:
    def __init__(self,n):
        self.values=n

    def __add__(self,m):
        return self.values+m.values
    def __sub__(self,m):
        return self.values-m.values
    def __mul__(self,m):
        return self.values*m.values
    def __truediv__(self,m):
        return self.values/m.values
    def __eq__(self,m):
        return self.values==m.values


n1=number(100)
n2=number(20)

print("Addition:",n1+n2)
print("Subtraction:",n1-n2)
print("Multiplication:",n1*n2)
print("Division:",n1/n2)
print("Equality:",n1==n2)
