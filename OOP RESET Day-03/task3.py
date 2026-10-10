class father:
    def skills(self):
        print("Father:Programming")

class mother:
    def hobby(self):
        print("Mother: gardening")

class child(father,mother):
    def play(self):
        print("Child: Playing")

c1=child()
c1.skills()
c1.hobby()
c1.play()
