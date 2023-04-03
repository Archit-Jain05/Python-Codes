count=0
i=1
while i in range(1,51):
	if(i%7==0):
		print(i)
		count+=1
	i+=1

print("Total number divisible by 7: ",count)