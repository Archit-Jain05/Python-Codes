def circle(radius):
    area=3.14*(radius**2)
    circ=2*3.14*radius
    return (area,circ)

print("Enter the radius of circle: ")
r=float(input())
a=circle(r)

print("Area = ",a[0]," Cirumference = ",a[1])

