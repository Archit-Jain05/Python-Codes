print("Enter number:")
n=float(input())

flag=True
for i in range(2,10):
    if(n%i==0 and n not in(2,3,5,7)):
        flag=False
    
if(flag==True):
    print("Prime")
else:
    print("Not prime")