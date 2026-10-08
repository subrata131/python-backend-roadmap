class student:
    def __init__(self,n,r,mark):
        self.name=n
        self.roll=r
        self.__mark=mark

    def get_mark(self):
        print("Mark is:",self.__mark)

    def set_mark(self,mar):

        if mar>=0 and mar<=100:
            self.__mark=mar
        else:
            print("Invalid")

s1=student("Subarta",101,90)
s1.get_mark()
s1.set_mark(110)
s1.get_mark()
s1.set_mark(-50)
s1.get_mark()




    
