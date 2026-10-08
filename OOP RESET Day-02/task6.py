class animal:
    def sounds(self):
        print("Animal makes sound")

class dog(animal):
    def sounds(self):
        print("Dog barks")

d1=dog()
a1=animal()
print(isinstance(d1,dog))
print(isinstance(d1,animal))
print(isinstance(a1,dog))
