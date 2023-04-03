#simple func
def hello():
	print("Hello World")

hello()
#func with parameter
def name(name):
	print("Hi",name)

name("Archit")
#func with parameter and return
def add(a,b):
	c=a+b
	return c

res=add(1,2)
print(res)