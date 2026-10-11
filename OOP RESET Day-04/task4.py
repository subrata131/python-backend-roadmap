class dog:
    def sound(self):
        print("Dog barks")

class cat:
    def sound(self):
        print("Cat meows")

d1=dog()
c1=cat()

animals=[d1,c1]
for i in animals:
    i.sound()
