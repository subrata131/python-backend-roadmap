class employee:
    def work(self):
        print("Employee is working")

class developer(employee):
    def work(self):
        print("Writing code")

class manager(employee):
    def work(self):
        print("Managing Team")

class tester(employee):
    def work(self):
        print("Testing software")

employee=[developer(), manager(), tester()]

for i in employee:
    i.work()
