t1=(1,2,1,1)

flag=True
for i in range(0,len(t1)):
    if t1[i]!=t1[i-1]:
        flag=False

if(flag==True):
    print("All elements are same")
else:
    print("All elements are not same")