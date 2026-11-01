class teacher:
    def __init__(self,n):
        self.name=n

    def teach(self):
        print(f"{self.name} is teaching")

class department:
    def __init__(self,t):
        self.teachers=t
    def show_teachers(self):
        for n in self.teachers:
            n.teach()

t1=teacher("subrata")
t2=teacher("sanjib")

d1=department([t1,t2])
d1.show_teachers()

        
