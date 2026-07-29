students=[]

# student={
#      "name":"",
#      "Mark":""
# }

def add_student():
    
    name=input("Enter student name:")
    # student.append["name"]=name
    try:

         mark=int(input("Enter Student mark:"))
         if mark<=0 or mark>=100:
              
              raise ValueError("Mark must be between 0 to 100")
         student={
              "name":name,
               "Mark":mark
            }
         students.append(student)
         
    except ValueError:
         print("Enter Number only")


def view_student():
     if len(students)==0:
          print("No student Found")
     else:
          for i in students:
               print("=================")
               print("Name:",i["name"])
               print("Mark:",i["Mark"])
     

while True:
     print("===Student Mark Manager===")
     print("\n1.Add student\n2.View Student\n3.Exit")
     n=int(input("Enter Your Choice:"))
     if n==1:
          add_student()
     elif n==2:
          view_student()
     elif n==3:
          break
     else:
          print("Invalid")
          

         
              