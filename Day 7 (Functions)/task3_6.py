# Write a python program to find number of occurrences of each vowel present in the given string?
"""
vowels = {}
lst = ['a','e', 'i','o', 'u']
sent = input("Enter a string ").lower()
for s in sent:
	if s in lst:
		if s in vowels:
			vowels[s] =  vowels[s] + 1
		else:
			vowels[s] = 1
print(vowels)
"""
vowels = {
	'a' : 0,
	'e' : 0,
	'i' : 0,
	'o' : 0,
	'u' : 0
}

sentence = input("Enter a Senetence ").lower()
for s in sentence:
	if s in vowels:
		vowels[s] += 1

for key,val in vowels.items():
	print(f"{key} = {val}")















