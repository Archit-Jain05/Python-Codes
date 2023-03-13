print("***Enter the marks out of 100***\n")
#a=b=c=d=e=f=0

dictc={"0 - 39":0,"40 - 49":0,"50 - 59":0,"60 - 69":0,"70 - 79":0,"80 - 100":0}

n=int(input("Enter the number of student marks to enter:"))

for n in range(0,n):
	print("Enter the marks of student",n+1)
	marks=int(input())
	if(marks>=0 and marks<=39):
		dictc["0 - 39"]+=1
	elif(marks>=40 and marks<=49):
		dictc["40 - 49"]+=1
	elif(marks>=50 and marks<=59):
		dictc["50 - 59"]+=1
	elif(marks>=60 and marks<=69):
		dictc["60 - 69"]+=1
	elif(marks>=70 and marks<=79):
		dictc["70 - 79"]+=1
	elif(marks>=80 and marks<=100):
		dictc["80 - 100"]+=1
	else:
		print("enter valid marks withing 0 - 100")

'''print("0 - 39 | 40 - 49 | 50 - 59 | 60 - 69 | 70 - 79 | 80 - 100")
print(" ",a,"	   ",b,"       ",c,"       ",d,"       ",e,"       ",f) '''

print(dictc)