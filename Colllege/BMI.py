print("Enter the Weight:")
w=float(input())
print("Enter the height in metres:")
h=float(input())

bmi=w/(h*h)

if(bmi<18.5):
	print("Underweight")
elif(bmi>=18.5 and bmi<=24.9):
	print("Healthy")
elif(bmi>=25 and bmi<=29.9):
	print("Overweight")
else:
	print("Obese")
	