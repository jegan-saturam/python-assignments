import re
password = input("Enter your password: ")
boolean = True
while boolean:  
	if not re.search("[a-z]",password):
		break
	elif not re.search("[0-9]",password):
		break
	elif not re.search("[A-Z]",password):
		break
	elif not re.search("[$#@]",password):
		break
	elif (len(password)<6 or len(password)>12):
		break
	elif re.search("\s",password):
		break
	else:
		print("Valid Password")
		boolean=False
if boolean:
	print("Invalid Password")