class vehicle:
    def start(self):
        print("Vehicle is starting")

class car(vehicle):
    def start(self):
        print("Car engine started")

class bike(vehicle):
    def start(self):
        print("Bike engine started")

class truck(vehicle):
    def start(self):
        print("Truck engine started")   

v=[car(),bike(),truck()]

for i in v:
    i.start()   

def start_vehicles(vehicles):
    for vehicle in vehicles:
        vehicle.start()
