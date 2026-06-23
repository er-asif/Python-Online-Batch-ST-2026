# Method overriding 

class Square():
    def area(self, side):
        print("Area of Square = ", side **2)

class Rectangle(Square):
    def area(self, l, b):
        print("Area of Rectangle =", l*b)

sq = Square()
sq.area(4)

rect = Rectangle()
rect.area(3,4)