n=int(input("Enter a year:"))
if n%4==0 and n%100!=0 or n%400==0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")