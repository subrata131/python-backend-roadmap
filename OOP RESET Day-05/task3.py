class fulltime:
    def calculate_salary(self):
        return 30000

class parttime:
    def calculate_salary(self):
        return 12000

f1=fulltime()
p1=parttime()
list=[f1,p1]
for i in list:
    print(i.calculate_salary())

