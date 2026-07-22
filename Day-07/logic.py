marks=(78,56,98,45,87,67)
max=marks[0]
min=marks[0]
for i in range(0,len(marks)):
    if marks[i]>max:
        max=marks[i]
    elif marks[i]<min:
        min=marks[i]

print("highest Marks:",max)
print("Lowest Marks:",min)
