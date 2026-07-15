cart=[]

while(True):
    print("1.Add Item\n2.Remove Item\n3.View Cart\n4.Search Item\n5.Exit\n")
    n=int(input("Enter Your choice:"))
    if n==1:
        m=input("Enter Item to Add:")
        cart.append(m)
    elif n==2:
        m=input("Enter Item to remove:")
        cart.remove(m)
    elif n==3:
        for i in cart:
            print(i)
    elif n==4:
        m=input("Enter Item to Search:")
        if m in cart:
            print(m,"Found")
        else:
            print(m,"Not Found")
    else:
        break
    