def switch(a,b,c):
    switcher = {
        1: print(a+b),
        2: print(a-b),
    }
    return switcher.get(c)

a=float(input("Enter number 1: "))
b=float(input("Enter number 2: "))

print("\n1. Add \n2. Subtract")

c=int(input("Enter your choice: "))
switch(a,b,c)

