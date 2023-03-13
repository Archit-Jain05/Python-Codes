import math

print("ax^2+bx+c")
print("Enter the value of a:")
a=int(input())
print("Enter the value of b:")
b=int(input())
print("Enter the value of c:")
c=int(input())

delta=(b*b)-(4*a*c)
print("Delta = ",delta)

if(delta>0):
	root1=(-b+math.sqrt(delta))/(2*a)
	root2=(-b-math.sqrt(delta))/(2*a)
	print("Root 1 = ",root1)
	print("Root 2 = ",root2)

elif(delta==0):
	root=(-b+math.sqrt(delta))/(2*a)
	print("Both roots are equal, Answer = ",root)
else:
	print("Roots are imaginary")
