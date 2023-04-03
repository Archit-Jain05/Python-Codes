#prime number

def prime(num):
	flag=True
	a=int(num)
	for i in range(2,a):
		if(num%i ==0):
			flag=False
			
	print("First loop activated")
	if(num>10):
		for i in range(a+1,11):
			if(num%i ==0):
				flag=False
				
		print("Second loop activated")
	if(flag==False):
		return 0
	else:
		return 1

print("Enter the number to check: ")
n=float(input())
res=prime(n)
if(res==0):
	print("Number is non prime")
else:
	print("Number is prime")