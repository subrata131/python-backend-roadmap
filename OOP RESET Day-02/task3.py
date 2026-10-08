class animal:
    def eat(self):
        print("Animal is eating")

class dog(animal):
    def berk(self):
        print("Dog is breaking")

d1=dog()
d1.eat()
d1.berk()
