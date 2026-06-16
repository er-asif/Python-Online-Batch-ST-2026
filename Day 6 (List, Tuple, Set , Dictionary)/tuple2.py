lst = []

for i in range(5):
	n = int(input("Enter a number "))
	lst.append(n)

tup = tuple(lst)
print("Tuple =", tup)
print(type(tup))
