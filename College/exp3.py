acc_no=int(input("Enter the account number: "))
name=input("Enter the name of the account holder: ")
age=int(input("Enter the age: "))


interest=0
while interest==0:
	gender=input('Enter the gender "Male" / "Female": ')
	if(age<60):
		if(gender in ("male","Male","m","M")):
			interest=0.04
		if(gender in ("Female","female","f","F")):
			interest=0.05
		if(gender not in("male","Male","m","M","Female","female","f","F")):
			interest=0
	if(age>60):
		interest=0.07

	if(interest==0):
		print("Enter valid gender!")

bal=int(input("Enter the account balance: "))

print("Name: ",name)
cal=bal*interest
print("Interest: ",cal,"$")
print("Total balance: ",bal+cal,"$")