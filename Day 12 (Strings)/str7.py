full_name = input("Enter your full name ")
words = full_name.split()
short_name = ""

for word in words[0:len(words)-1]:
    short_name = short_name + word[0] + ". "

short_name = short_name + words[-1]

print(short_name)


