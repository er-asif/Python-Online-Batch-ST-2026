full_name = input("Enter your full name ")
words = full_name.split()
short_name = ""

# full_name = "Mohandas Karamchandra Gandhi"
# short_name = M. K. Gandhi
# full_name.split() => ['Mohandas', 'Karamchandra', 'Gandhi'] => 3
# for word in words[0:2]:
#   short_name = "M. " + "K" + ". "  # M.K. 
 
for word in words[0:len(words)-1]:
    short_name = short_name + word[0] + ". "

short_name = short_name + words[-1]

print(short_name)


