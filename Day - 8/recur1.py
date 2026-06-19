# Recursion 
# When a function call itself, it is known as recursion.


def fact(n):
	if n==1:
		return 1	
	return n * fact(n-1)	
print(fact(4))

# 4 * fact(3)
# 4 * 3 * fact(2)
# 4 * 3 * 2 * fact(1)
# 4 * 3 * 2 * 1