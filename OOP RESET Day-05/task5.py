class rectangle:
    def __init__(self,l,w):
        self.len=l
        self.wid=w
    def area(self):
        return self.len*self.wid

        
        

class circle:
    def __init__(self,r):
        self.ra=r

    def area(self):
        return 3.14*self.ra*self.ra

r1=rectangle(10,5)

c1=circle(7)
shapes=[r1,c1]
for i in shapes:
    print(i.area())
