attendance=set()
def add():
    name=input("Enter Student Name:")
    attendance.add(name)
    print("Student Added Sucessfully")

def view():
    for i in attendance:
        print(i)

def search():
    n=input("Enter Student Name To Search:")
    if n in attendance:
        print("Present")
    else:
        print("Absent")

def total():
    print(len(attendance))

    
while True:
    print("====Attendance System====")
    print("\n1.Mark Attendance\n2.View Attendance\n3.Search Student\n4.Total Student Present\n5.Exit\n")
    n=int(input("Enter Your Choice:"))
    if n==1:
        add()
    elif n==2:
        view()
    elif n==3:
        search()
    elif n==4:
        total()
    elif n==5:
        break
    else:
        print("Invalid")
