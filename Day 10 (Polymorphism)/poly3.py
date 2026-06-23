# Method Overloading 
# Default parameters 

class Shape():
    def area(self, a=None, b=None):
        if a is not None and b is None:
            print("Area of Square =", a**2)
        elif a is not None and b is not None:
            print("Area of Rectangle =", a*b)

sh = Shape()
sh.area(5)
sh.area(2,3)