try:
    with open("student.txt","r") as file:

      print(file.read())
except FileNotFoundError:
    print("file Not Found")
finally:
    print("Thank You")
