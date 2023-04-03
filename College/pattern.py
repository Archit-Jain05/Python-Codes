c1=0
c2=0
i=1
n=1
level=int(input("Enter the number of levels yopu want:"))

while i in range(1,level+1):

	while n in range(1,i+1):
		print(n,end="")
		n=n+1
	print()
	i=i+1