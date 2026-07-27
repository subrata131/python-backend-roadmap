def add():
    try:
        n=int(input("Enter Your First Number:"))
        m=int(input("Enter Your Second Number:"))
        print("Sum is:",n+m)
    except ValueError:
        print("Enter Number Only")
def sub():  
    try:
        n=int(input("Enter Your First Number:"))
        m=int(input("Enter Your Second Number:"))
        print("Sum is:",n-m)
    except ValueError:
        print("Enter Number Only")

def mul(): 
    try:
        n=int(input("Enter Your First Number:"))
        m=int(input("Enter Your Second Number:"))
        print("Sum is:",n+m)
    except ValueError:
        print("Enter Number Only")

def div(): 
    try:
        n=int(input("Enter Your First Number:"))
        m=int(input("Enter Your Second Number:"))
        print("Sum is:",n/m)
    except ZeroDivisionError:
        print("Cannot Divide by Zero")
    
    



while True:
    print("===Simple Calculator===")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    n=int(input("Enter Your choice:"))
    if n==1:
        add()
    elif n==2:
        sub()
    elif n==3:
        mul()
    elif n==4:
        div()
    elif n==5:
        break
    else:
        print("Invalid input")