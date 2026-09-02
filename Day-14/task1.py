class animal:
    def sound(self):
        print("Animal makes a sound")

class dog(animal):
    def sound(self):
        print("barks")

class cat(animal):
    def sound(self):
        print("meows")


d=dog()
d.sound()
c=cat()
c.sound()

        
