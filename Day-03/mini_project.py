pas="Jadab@123"
count=0
while count<3:
    n=input("Enter Your Password:")
    if pas==n:
        print("Login Successful")
        break
    elif count==2:
        print("Account Locked")
        break
    else:
        print("Wrong password\nTry Again")
        
    count+=1
    # if count==3:
    #     print("Account Locked")
