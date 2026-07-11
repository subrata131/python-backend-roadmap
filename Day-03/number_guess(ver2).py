n=25
count=0
while count<5:
    m=int(input("Guess The Number:"))
    if n==m:
        print("Congratulations!!")
        break
    elif n>m:
        print("Too Low")
    elif n<m:
        print("Too High")
   
    
    count+=1

    if count==5 and n!=m:
        print("The number is:",n)
