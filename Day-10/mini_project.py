while True:
    print("===Notes Manager===")
    print("\n1.Add Note\n2.View Notes\n3.Exit\n")
    n=int(input("Enter Your Choice:"))
    if n==1:
        m=input("Enter your Notes:")
        file=open("notes.txt","a")
        file.write("\n"+m)
        file.close()
        print("Note Added Sucessfully")
    elif n==2:
        with open("notes.txt","r") as file:
            for i in file:
                print(i.strip())
    elif n==3:
        break
    else:
        print("Invaild Input")

        