sentence = input("Enter the Sentence: ")
upper=0
lower=0
spaces=0
for character in sentence:
	if character.isupper():
		upper+=1
	elif character.islower():
		lower+=1
	elif character.isspace():
		spaces+=1
print("No of UpperCase: ",upper)
print("No of LowerCase: ",lower)
print("No of Spaces: ",spaces)