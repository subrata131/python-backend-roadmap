name=input("Enter your name:")
n=int(input("Enter your Marks:"))

print("Name:",name)
print("Marks:",n)

if n>=40:
    print("Status: Pass")
    if n>=90 and n<=100:
         print("Your Grade is \"A\"")
    elif n>=75 and n<=89:
         print("Your Grade is \"B\"")
    elif n>=60 and n<=74:
         print("Your Grade is \"C\"")
    elif n>=40 and n<=59:
         print("Your Grade is \"D\"")
else:
    print("Fail")