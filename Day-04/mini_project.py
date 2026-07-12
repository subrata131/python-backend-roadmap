def input_student():
    n=input("Enter student Name:")
    return n
def calculate():
    m=int(input("Enter your marks for sub-1:"))
    n=int(input("Enter Your Mark for sub-2:"))
    o=int(input("Enter Your mark for Sub-3:"))

    ave=(m+n+o)/3

    if ave<=100 and ave>=90:
        return "A"
    elif ave<90 and ave>=75:
        return "B"
    elif ave<75 and ave>=60:
        return "C"
    elif ave<60 and ave>=40:
        return "D"
    else:
        return "F"
    
def display():
    print("Student Name:",input_student())
    print("Grade is:",calculate())

display()

    