class livingthing:
    def __init__(self,name):
        self.name=name

    def show(self):
        print("I am a living thing and my name is",self.name)

class animal(livingthing):
    def __init__(self,sound):
        self.sound=sound

    def show(self):
        print("I am an animal and I make",self.sound,"sound")

class dog(animal):
    def __init__(self,breed):
        self.breed=breed

    def show(self):
        print("I am a dog and my breed is",self.breed)

name=livingthing("Jadab")
name.show()