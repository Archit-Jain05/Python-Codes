import math


math.factorial(3)

print("Enter the value of x: ")
x=int(input())
print("Enter the value of n: ")
n=int(input())
ans=0
if(n==1):
	ans=ans+1
	print("Answer = ",ans)
elif(n>=2):
	ans=ans+1
	i=1
	while i in range(1,n):
		ans=ans+(x**i)/(math.factorial(i))
		i=i+1
	print("Answer = ",ans)
		

else:
	print("Please Enter positive n")