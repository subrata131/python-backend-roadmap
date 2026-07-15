fruits=["apple","banana","lichi","coconut"]
n=input("Enter a fruit to search:")
n1=n.lower()
if n1 in fruits:
    print("Found")
else:
    print("Not Found")