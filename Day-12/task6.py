class book:
    def __init__(self,title,author,price=500):
        self.title=title
        self.author=author
        self.price=price

    def show(self):
        print("Book title:",self.title)
        print("Book Author:",self.author)
        print("Book Price:",self.price)

b1=book("Python","Guido")
b2=book("C","Dennis",350)

b1.show()
b2.show()


