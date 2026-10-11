class animal:
    def sound(self):
        print("Animal makes a sound")

class dog(animal):
    def sound(self):
        print("Dog barks")

class cat(animal):
    def sound(self):
        print("Cat meows")

c1=cat()
d1=dog()

a=[d1,c1]
for i in a:
    i.sound()
