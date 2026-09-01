class shape:
    def area(self, length, width):
        print("area of shape", length * width)

class rectangle(shape):
    def area(self, length, width):
        print("area of rectangle", length * width)

a=shape()
a.area(5,40)
