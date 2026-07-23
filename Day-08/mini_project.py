student={
   
}
def add_student():
        n=int(input("Enter Roll Number:"))
        name=input("Enter Student Name:")
        age=int(input("Enter your age:"))
        mark=int(input("Enter your marks:"))
        student[n]={
             "name":name,
             "age":age,
             "marks":mark
        }


def view_student():
     for i,j in student.items():
          print(i,"=",j)

def search_student():
     n=int(input("Enter Student Roll Number:"))
     if n in student:
          print(student[n])
     else:
          print("Student Not Found")

def delete_student():
     n=int(input("Enter Student Roll to Delete:"))
     if n in student:
          del student[n]
     else:
          print("Student Not Found")


def update_student():
     n=int(input("Enter Student Roll Number To Update:"))
     if n in student:
          m=int(input("Enter Your Updated Mark:"))
          student[n]["marks"]=m
     else:
          print("Student Not Found")
     

while True:
    print("====Student Record System====")
    print("\n1.Add Student\n2.View Student\n3.Search Student\n4.Update Student\n5.Delete Student\n6.Exit")

    n=int(input("Enter Your choice:"))


    if n==1:
        add_student()
    elif n==2:
         view_student()
    elif n==3:
         search_student()
    elif n==4:
         update_student()
         
    elif n==5:
         delete_student()
    elif n==6:
         break
    else:
         print("Invalid")
