# Write a python program to find sum of digits of given number.

num = int(input("Enter a number ")) 
sum = 0
while num>0:
	digit = num % 10  
	sum += digit       
	num = num // 10	 
print("Sum of Digits =", sum)