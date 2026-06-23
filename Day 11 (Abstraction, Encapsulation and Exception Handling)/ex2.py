dict = {
    'python' : "Python is an interpreted, object oriented, high level prgramming lang.",
    'int' : "Integer datatype",
    'function' : "Block of  code used to perform any task."
}

word = input("Enter word to search : ")

try:
    print(dict[word])
except KeyError:
    print("Word not found !!")

