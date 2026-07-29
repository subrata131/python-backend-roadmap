
m=0
n=0
while n<10:
    try:
        n=int(input("Enter number To sum:"))
        m+=n
        n+=1
       
    except ValueError:
        print("Enter Number only:")


print("Sum is:",m)

    