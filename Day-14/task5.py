class laptop:
    def start(self):
        print("Laptop is starting")

class car:
    def start(self):
        print("Car is starting")

def start_devices(devices):
    for device in devices:
        device.start()
    
