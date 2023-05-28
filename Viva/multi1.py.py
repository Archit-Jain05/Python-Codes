import threading
from threading import *

def count(start,end):
    for i in range(start,end+1):
        print(i)

t1=Thread(target=count,args=(1,10))
t2=Thread(target=count,args=(11,20))

t2.start()

t2.join()
t1.start()
t1.join()