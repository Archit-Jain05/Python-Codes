def area(r,pi=3.14):
	area=pi*r*r  
	return area

print("Enter radius:")
radius=float(input())
print("Do you want to enter value of pi?\nY\nN")
choice=input()

if(choice=="Y"):
	print("Enter the value of pi:")
	p=float(input())
	print("Area = ",area(radius,p))
elif(choice=="N"):
	print("Area = ",area(radius))
else:
	print("Invalid choice")
