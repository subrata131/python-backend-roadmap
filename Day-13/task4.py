class person:
    def __init__(self,name):
        self.name=name

    def show(self):
        print("I am", self.name)

class teacher(person):
    def __init__(self,sub):
        self.sub=sub

    def show(self):
        print("I am a teacher of",self.sub)

s=person("subrata")
y=teacher("math")
print(isinstance(s,person))
print(isinstance(y,teacher))
