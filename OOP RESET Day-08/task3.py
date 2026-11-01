class doctor:
    def __init__(self,n):
        self.name=n

class patient:
    def __init__(self,n):
        self.name=n

    def consult(self,d):
        print(f"{self.name} consulted Dr.{d.name}")

d1=doctor("Subrata")
p1=patient("Sanjib")
p1.consult(d1)

