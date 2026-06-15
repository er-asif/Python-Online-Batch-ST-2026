"""
Write a python program to find roots of quadratic equation ax^2+bx+c=0.
root1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
root2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
"""

import cmath

a = int(input("Enter coefficient of X^2 :"))
b = int(input("Enter coefficient of X : "))
c = int(input("Enter constant: "))

root1 = (-b+cmath.sqrt(b*b-4*a*c))/(2*a)
root2 = (-b-cmath.sqrt(b*b-4*a*c))/(2*a)

print("Root 1 =", root1)
print("Root 2 =", root2)

