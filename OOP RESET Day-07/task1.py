class cpu:
    def process(self):
        print("CPU is processing")

class computer:
    def __init__(self):
        self.cpu=cpu()

    def run(self):
        self.cpu.process()

c1=computer()
c1.run()
