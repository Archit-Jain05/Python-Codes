def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def select(choice,a,b):
    switcher={
        1:add,
        2:sub
    }
    #return switcher.get(choice)(a,b)

print(select(2,4,4))

#remove all comments for execution