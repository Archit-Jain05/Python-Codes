def bmi(w,h):
	bmi=w/(h*h)
	return bmi

print("Enter the weight in kgs: ")
weight=float(input())
print("Enter the height in metres")
height=float(input())

print(bmi(weight,height))

