# Palindrome String
str1 = input("Enter a string ").lower()

if str1 == str1[::-1]:
    print("It is Palindrome")
else:
    print("Not palindrome")