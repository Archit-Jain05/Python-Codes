class person:
    def __init__(self,num):
        print("Object",num,"created")


aob=[]
n=int(input("Enter number of objects to create:"))
for i in range(0,n):
    a=person(i+1)
    aob.append(a)

