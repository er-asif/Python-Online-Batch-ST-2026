# Read and Write both

file = open("emp.txt", "a+")
file.write("\nThis is updated")
file.seek(0)
data = file.read()
print(data)

file.close()