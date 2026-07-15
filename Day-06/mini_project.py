marks=[]
sum=0
while(True):
    print("1.Add Marks\n2.View Marks\n3.Highest Marks\n4.Lowest Marks\n5.Average Marks\n6.Exit")

    n=int(input("Enter your choice:"))
    if n==1:
        m=int(input("Enter Your marks:"))
        marks.append(m)
    elif n==2:
        print(marks)
    elif n==3:
        marks.sort()
        print("Highest Mark is:",marks[-1])
    elif n==4:
        marks.sort()
        print("Lowest mark is:",marks[0])
    elif n==5:
        for i in marks:
            sum+=i
        print("Average is:",(sum/len(marks)))
    else:
        break