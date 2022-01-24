sentence = input("Enter the Sentence: ")
letters=0
digits=0
for character in sentence:
	if character.isalpha():
		letters+=1
	elif character.isdigit():
		digits+=1
print("No of Letters: ",letters)
print("No of Digits: ",digits)