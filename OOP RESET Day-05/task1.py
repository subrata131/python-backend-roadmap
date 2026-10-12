class dog:
    def sound(self):
        print("Dog barks")

class robot:
    def sound(self):
        print("Robot makes a sound")

d1=dog()
r1=robot()
list=[d1,r1]
for i in list:
    i.sound()

