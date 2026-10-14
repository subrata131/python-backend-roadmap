class engine:
    def start(self):
        print("Engine started")

class music:
    def play(self):
        print("Music is Playing")

class car:
    def __init__(self):
        self.e=engine()
        self.m=music()

    def drive(self):
        self.e.start()
        self.m.play()

c1=car()
c1.drive()
