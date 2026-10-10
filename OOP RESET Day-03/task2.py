class animal:
    def eat(self):
        print("Animal is eating")

class dog(animal):
    def bark(self):
        print("Dog is barking")

class cat(animal):
    def meow(self):
        print("Cat is meowing")


d1=dog()
c1=cat()
d1.eat()
c1.eat()
d1.bark()
c1.meow()
