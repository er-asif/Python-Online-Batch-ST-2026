# how to create list by taking inputs from user

nums = []

for i in range(5):
	n = int(input(f"Enter {i} th element "))
	#nums.append(n)
	nums.insert(n, i)

print(nums)