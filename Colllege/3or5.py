list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in range(0,len(list)):
	if(list[i]%3==0 or list[i]%5==0):
		print(list[i])
	i=i+1