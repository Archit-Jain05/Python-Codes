list1=[1,2,10,4,5,6,7,8]
largest=list1[0]
smallest=list1[0]
for e in list1:
	if(smallest>e):
		smallest=e

print("Smallest = ",smallest)

for e in list1:
	if(largest<e):
		largest=e

print("largest = ",largest)
