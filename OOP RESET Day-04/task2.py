class animal:
    pass
class dog(animal):
    pass

d1=dog()
print(isinstance(d1,dog))
print(isinstance(d1,animal))
print(issubclass(dog,animal))
print(issubclass(animal,dog))
