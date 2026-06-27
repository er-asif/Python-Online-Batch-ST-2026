file_name = input("Enter file name to create ")
with open(file_name, "w+") as file:
    print("File created successfully")
    data = input("Enter content to insert ")
    file.write(data)
    print("Data inserted successfully")
