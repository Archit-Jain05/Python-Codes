from collections.abc import Callable, Iterable, Mapping
from threading import *
from typing import Any

class Count(Thread):
    counter=0

    def __init__(self,s,e):
        Thread.__init__(self)
        self.s=s
        self.e=e

    def run(self):
           for i in range(self.s,self.e+1):
            print(i)
            self.counter+=1
    

c1=Count(1,10)
c2=Count(11,20)
c1.start()
c1.join()
c2.start()
c2.join()
print(c1.counter+c2.counter)