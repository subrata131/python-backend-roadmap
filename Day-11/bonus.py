username="admin"
password=1234
att=0
while att < 3:
    n=input("Enter Username:")
    m=int(input("Enter Password:"))
    if n==username and m==password:
        print("Login Successfully")
        break
    elif att==2:
        print("Locked")
    att+=1
