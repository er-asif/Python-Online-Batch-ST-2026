# Exception Handling

try:
    n1 = int(input("Enter 1st number "))
    n2 = int(input("Enter 2nd number "))
    div = n1/n2
    print("Division =", div)
except ValueError:
    print("Enter only numbers")
except ZeroDivisionError:
    print("you cannot divide by zero")
finally:
    print("Program executed successfully")
