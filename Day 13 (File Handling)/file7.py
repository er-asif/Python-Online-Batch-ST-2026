# reading file by taking user's input

file_name = input("Enter file name to open ")
try:
    with open(file_name, "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("This file does not exists.")