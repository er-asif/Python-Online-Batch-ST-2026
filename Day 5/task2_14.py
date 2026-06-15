#  Write a python program to print Fibonacci series up to n terms, where value of n is entered by user.
# 0, 1, 1, 2, 3, 5, 8....... 

num = int(input("Enter no. of terms "))
n1 = 0
n2 = 1
print(n1, end=" ")
print(n2, end=" ")
for i in range(3, num+1):
	next = n1+n2
	print(next, end=" ")
	n1 = n2
	n2 = next 

	

