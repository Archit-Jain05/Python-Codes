import sys

my_path="E:\T001\Python\T1"
if my_path not in sys.path:
   sys.path.append(my_path)
#print(sys.path)


from T1 import mymath
print(mymath.fact(4))
