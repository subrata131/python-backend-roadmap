try:
    n=int(input("Enter First Number:"))
    m=int(input("Enter Second Number:"))
    print("Sum is:",n+m)
except ValueError:
    print("Please Enter Number Only")