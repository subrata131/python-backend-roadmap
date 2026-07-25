for i in range(5):
    n=input("Enter Your name:")
    with open("names.txt","a") as file:
        file.write("\n\n"+n)

with open("names.txt") as file:
    for i in file:
        print(i.strip())
