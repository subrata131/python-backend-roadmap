password=input("Enter Your Password:")
upper=False
digit=False
for i in password:
    if i.isupper():
        upper=True
    elif i.isdigit():
        digit=True

if len(password)>=8 and upper and digit:
    print("Password Strong")
else:
    print("Weak password")
 
