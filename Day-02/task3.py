a=int(input("Enter First number:"))
b=int(input("Enter Second number:"))          
c=int(input("Enter Third number:"))

if a>=b and a>=c:
    print("The largest number is:",a)
elif b>=a and b>=c:
    print("The largest Number is:",b)
else:
    print("The Largest number is:",c)

if a<=b and a<=c:
    print("THe smallest numberis:",a)
elif b<=a and b<=c:
    print("The smallest number is;",b)
else:
    print("The smallest number is:",c)