import random

ch = int(input("Enter number 1-5 "))
num = random.randint(1,5)
if ch == num:
	print("Congratulations !! You won the game!!")
else:
	print("Better luck next time !!")
	print(f"Number - {num} -- Input - {ch} ")
