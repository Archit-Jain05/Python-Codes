from multipledispatch import dispatch

@dispatch(int,int)
def multiply(a,b):
    print("2 Num")

@dispatch(int,int,int)
def multiply(a,b,c):
    print("3 Num")

@dispatch(float,float,float)
def multiply(a,b,c):
    print("3 Float") 

multiply(5,5)
multiply(7,5,30)
multiply(2.0,4.2,3.5)