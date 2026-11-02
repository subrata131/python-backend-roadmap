class number:
    def __init__(self,values):
        self.values=values

    def __add__(self,n):
        return self.values+n.values

n1=number(50)
n2=number(30)
print(n1+n2)

