matchstr = input("Enter the text: ")
contents = open("extext.txt", "r")
print(contents)

for line in contents:
	line = line.strip()
	splitcontents = line.split(" ")
for words in splitcontents:
	if words.lower() == matchstr.lower():
		print("True")
		break
