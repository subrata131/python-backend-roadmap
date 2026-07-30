class student:
    def __init__(self,name,roll,mark):
        self.name=name
        self.roll=roll
        self.mark=mark

    def show(self):
        print("student Name:",self.name)
        print("Student Roll:",self.roll)
        print("Student Mark:",self.mark)
students=[]
while True:
    print("===Student Manager===")
    print("\n1.Add Student\n2.View Student\n3.Exit")
    n=int(input("enter Your Choice:"))
    if n==1:
        name=input("Enter Your name:")
        roll=int(input("Enter Your Roll Number:"))
        mark=int(input("Enter Your Mark:"))
        s1=student(name,roll,mark)
        students.append(s1)
    elif n==2:
        s1.show()
    elif n==3:
        break
    else:
        print("Invaild")


