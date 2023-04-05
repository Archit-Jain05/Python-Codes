
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=0
try:
    c=a/b
    F=open("file1.txt","r")
    
except (ZeroDivisionError,IOError) as e:
    print(e)

else:
    print(c)

