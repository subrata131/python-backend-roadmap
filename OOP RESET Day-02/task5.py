class animal:
    def sounds(self):
        print("Animal makes sound")

class dog(animal):
    def sounds(self):
        print("Dog barks")

d1= dog()
d1.sounds()
