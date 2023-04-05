
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=0
try:
    c=a/b
except ZeroDivisionError as e:
    print("Division by zero",e)

else:
    print(c)

