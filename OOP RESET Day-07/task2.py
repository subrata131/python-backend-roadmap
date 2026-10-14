class cpu:
    def process(self):
        print("CPU is processing")

class ram:
    def load(self):
        print("RAM is loading data")

class computer:
    def __init__(self):
        self.c=cpu()
        self.r=ram()

    def run(self):
        self.c.process()
        self.r.load()

c1=computer()
c1.run()
