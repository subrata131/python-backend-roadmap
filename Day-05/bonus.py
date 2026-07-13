n=input("Enter a word:")
n1=n.lower()
count=0
count1=0
for i in n1:
    if  i in "aeiou":
        
        count+=1

    else:
        # print("consonant are:",i)
        count1+=1

print("Vowels :",count)
print("Consonat :",count1)
    