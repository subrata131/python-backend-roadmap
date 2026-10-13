from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class rectangle(shape):
    def __init__(self,l,w):
        self.len=l
        self.wid=w

    def area(self):
        return self.len*self.wid

class circle(shape):
    def __init__(self,r):
        self.rad=r

    def area(self):
        return 3.14*self.rad*self.rad

r1=rectangle(10,5)
print(r1.area())
c1=circle(5)
print(c1.area())
