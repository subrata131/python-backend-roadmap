class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        area=self.length*self.width
        print("Area is:",area)

    def peri(self):
        per=2*(self.length + self.width)
        print("Perimeter:",per)

r=rectangle(10,5)
r.area()
r.peri()
