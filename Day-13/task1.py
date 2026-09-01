class animal:
    def sound(self):
        print("some sound")

class dog(animal):
    def sound(self):
        print("bark")


a=animal()
b=dog()
a.sound()
b.sound()