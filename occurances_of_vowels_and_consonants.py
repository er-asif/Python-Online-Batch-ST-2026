str1 = input("Enter a string ") 
list1 = ['a', 'i', 'e', 'o', 'u']

vowels = {}
consonants = {}

for ch in str1.lower():
    if ch in list1:
        # insert in vowels
        if ch in vowels:
            vowels[ch] += 1
        else:
            vowels[ch] = 1
    else:
        if ch in consonants:
            consonants[ch] += 1
        else:
            consonants[ch] = 1

print(vowels)
print(consonants)