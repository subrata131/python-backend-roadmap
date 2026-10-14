class teacher:
    def __init__(self,n):
        self.name=n

    def teaches(self):
        print(f"{self.name} is teaching")

class deparment:
    def __init__(self,t):
        self.tea=t

    def show(self):
        self.tea.teaches()


t1=teacher("sub")
d1=deparment(t1)
d1.show()
