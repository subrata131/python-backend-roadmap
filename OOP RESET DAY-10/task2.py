class student:
    collage="Brainware University"

    @classmethod
    def change_collage(cls,new):
        cls.collage=new

    @classmethod
    def show_collage(cls):
        print("Collage name is:",cls.collage)

student.change_collage("ABC collage")
student.show_collage()