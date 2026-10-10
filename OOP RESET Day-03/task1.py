class animal:
    def eat(self):
        print("Animal is Eating")

class mammal(animal):
    def walk(self):
        print("Mammal is Walking")

class dog(mammal):
    def bark(self):
        print("Dog is Barking")

d1=dog()
d1.eat()
d1.walk()
d1.bark()
