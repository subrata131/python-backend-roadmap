class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def display(self):
        print("Name:",self.name)
        print("Mark:",self.mark)

s1=student("Subrata",90)
s1.display()
s2=student("Rahul",85)
s2.display()