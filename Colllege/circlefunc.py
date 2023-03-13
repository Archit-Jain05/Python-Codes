def calcirc(r):
	d=r*2
	p=2*3.14*r
	a=3.14*r*r
	return (d,p,a)
	'''print("Diameter = ",d)
	print("Perimeter = ",p)
	print("Area = ",a)'''

print("Enter the radius of the circle: ")
radius=float(input())

a=calcirc(radius)
#print(a)
print("Diameter = ",a[0])
print("Perimeter = ",a[1])
print("Area = ",a[2])