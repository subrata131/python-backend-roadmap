n=int(input("Enter your Mark:"))
if n<=0 or n>=100:
    raise ValueError("Mark Must be Between 0 and 100")