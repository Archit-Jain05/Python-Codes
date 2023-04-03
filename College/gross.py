#calculate gross salary of employee

def gross(b):
	gross=b+(0.65*b)+(0.39*b)+(0.07*b)
	return gross

print("Enter the code of the employee:")
code=input()
print("Enter the name of the employee:")
name=input()
print("Enter the basic salary:")
bsal=float(input())

gs=gross(bsal)
print("Gross salary = ",gs)