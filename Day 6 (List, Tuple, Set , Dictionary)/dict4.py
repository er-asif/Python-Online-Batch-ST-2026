dict1 = {}

for i in range(3):
	key = input("Enter Key ") 
	val = input("Enter value ")
	dict1[key] = val

for key, val in dict1.items():
	print(f"{key} = {val}")