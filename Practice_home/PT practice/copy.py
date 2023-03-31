l1={1:"hi",2:"hello"}
print(id(l1))
l2=l1.copy()
print(id(l2))

l3=l1.copy()
print(id(l3))

l1.update({2:"Hoioi"})
print(l1.setdefault(2,"efngjn"))
print(l1)

print(l2)