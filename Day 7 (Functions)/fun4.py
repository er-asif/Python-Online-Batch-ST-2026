# Simple Calculator
def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mult(a,b):
	return a*b
def div(a,b):
	return a/b

n1 = int(input("Enter 1st number "))
n2 = int(input("Enter 2nd number "))
print("""
Press 1 for addition
Press 2 for substraction
Press 3 for multiplication
Press 4 for division 
""")
ch = int(input("Enter your choice .... "))
if ch == 1:
	print("Summation =", add(n1,n2))
elif ch == 2:
	print("Substraction =", sub(n1,n2))
elif ch == 3:
	print("Multiplication =", mult(n1,n2))
elif ch == 4:
	print("Division =", div(n1,n2))
else:
	print("Invalid Choice")







