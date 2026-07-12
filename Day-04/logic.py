def add():
    n=int(input("Enter Your first Number:"))
    m=int(input("Enter Your Second Number:"))
    print(n,"+",m,"=",n+m)

def sub():
    n=int(input("Enter Your first Number:"))
    m=int(input("Enter Your Second Number:"))
    print(n,"-",m,"=",n-m)

def mul():
    n=int(input("Enter Your first Number:"))
    m=int(input("Enter Your Second Number:"))
    print(n,"*",m,"=",n*m)

def div():
    n=int(input("Enter Your first Number:"))
    m=int(input("Enter Your Second Number:"))
    print(n,"/",m,"=",n/m)

while True:
    print("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")
    n=int(input("Enter Your Choice:"))

    if n==1:
        add()
    elif n==2:
        sub()
    elif n==3:
        mul()
    elif n==4:
        div()
    else:
        break
    
        
        
