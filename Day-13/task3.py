class vehicle:
    def start(self):
        print("vehicle started")

class bike(vehicle):
    def start(self):
        print("bike started")

a=vehicle()
b=bike()

a.start()
b.start()