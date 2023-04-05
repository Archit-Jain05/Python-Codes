
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=0
try:
    c=a/b
except Exception:
    print("Division by zero",Exception)

else:
    print(c)

