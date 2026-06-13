'''
Write a python program to take number of days as input now display years, weeks
and days. E.g. If user input 375 days then output will be 1 years, 1 weeks and 3 days.
In this program ignore leap year

'''
days = int(input("Enter no. of days "))

y = days // 365
w = (days % 365) // 7
d = (days % 365) % 7

print("Years =",y)
print("Weeks =",w)
print("Days =",d)
