while True:
    print("1.Write Dairy\n2.Read Dairy\n3.Exit")
    n=int(input("Enter Your choice:"))
    if n==1:
        m=input("Enter:")
        with open("dairy.txt","a") as file:
            file.write("\n"+m)
    elif n==2:
        with open("dairy.txt","r") as file:
            for i in file:
                print(i.strip())
    elif n==4:
        break
    else:
        print("Invalid Input")

