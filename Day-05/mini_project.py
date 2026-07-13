name=input("Enter Your name:")
roll=int(input("Enter your roll Number:"))
dept=input("Enter your department:")
name1=name.upper()
id=dept.upper()+str(roll)[:3]+name1[:3]
print( "==== Student ID ====")
print("Name:",name)
print("Roll:",roll)
print("Dept:",dept.upper())

print("Student ID:",id)
print("===================")