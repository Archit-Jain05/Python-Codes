list1=['Hi','Hello','Bye','Hi']
print("Orignal list: ",list1)
list2=[]
for e in list1:
	if(list2.count(e)<1):
		list2.append(e)
print('Copied list:  ',list2)