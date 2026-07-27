try:
    n=int(input("enter a number to Square:"))
    print(n*n)
except ValueError:
    print("Enter Number Only")
else:
    print("Correct Input")