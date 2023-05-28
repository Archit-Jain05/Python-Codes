from threading import *

class count:
    counta=0

    def counter(self,s,e):
        for i in range(s,e+1,2):
            print(i)
            self.counta+=1

c1=count()
c2=count()
t1=Thread(target=c1.counter,args=(1,10))
t2=Thread(target=c2.counter,args=(11,20))
t1.start()
t1.join()
t2.start()
t2.join()
print("Total elements counted: ",c1.counta+c2.counta)