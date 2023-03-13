email=input("Enter the email id:")
validity =False
if('@' in email):
	if('.' in email):
		validity=True

if(validity==True):
	print("Entered email is correct")
else:
	print("Entered email is incorrect")