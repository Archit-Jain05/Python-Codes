list1=[1,2,3,6,4,3,6,3,2,6,1]
print(list1)
item=int(input("Enter the number to remove: "))

for i in list1:
	if item==i:
		list1.remove(i)

print(list1)