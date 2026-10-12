class dog:
    def sound(self):
        print("Dog barks")

class cat:
    def sound(self):
        print("Cat meows")

def make_sounds(animal):
    animal.sound()

d1=dog()
c1=cat()
make_sounds(d1)
make_sounds(c1)
