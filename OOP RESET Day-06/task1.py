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


r1=rectangle(10,5)
print(r1.area())

