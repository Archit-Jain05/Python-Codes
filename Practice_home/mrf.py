from functools import reduce

a=[1,2,3,4,5]

result=list(filter(lambda x:x>=3,a))

print(result)

r2=[i for i in a if i>=3]
print(r2)