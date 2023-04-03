class Demo:
    """"Demo Class"""
    classvar=0
    def __init__(self,a,b):
        print("Inisde constructor")
        self.a=a
        self.b=b

Demo(2,3)
print(Demo.__doc__)
print(Demo.__name__)
print(Demo.__dict__)
#hi