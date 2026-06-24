str1 = input("Enter a string ")

print("Is Upper =", str1.isupper())
print("Is Lower =", str1.islower())
print("Is title =", str1.istitle())
print("Is Aplpha Numeric =", str1.isalnum())

names = ["Mohammad Asif", "Mohammad Kaif", "Virat Kohli", "Aman Chaurasiya", "John Doe"]

for name in names:
    if name.startswith("Mohammad"):
        print(name)

for name in names:
    if name.endswith("Chaurasiya"):
        print(name)