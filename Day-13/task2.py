class person:
    def __init__(self,name):
        self.name=name

    def show(self):
        print("I am a person and my name is",self.name)
        
class teacher(person):

    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

teacher1=teacher("subrata", "math")


teacher1.show()


