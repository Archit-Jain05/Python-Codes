i=1
c=0
while i in range(1,51):
	if(i%7==0):
		c=c+1
	i=i+1

print("Count of numbers divisible by 7 between 1 to 50: ",c)