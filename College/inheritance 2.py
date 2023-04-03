class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
class Sports:
    def __init__(self):
        spoints=0

    def getSPoints(self):
        print("Which level have you represented: ")
        print("1. National \n2.State \n3.District\n4.Other")
        level=int(input())
        if(level==1):
            spoints=25
        elif(level==2):
            spoints=15
        elif(level==3):
            spoints=5
        else:
            spoints=0
        return spoints

    def choice(self):
        print("Have you participated in any sports? Y/N")
        c=input()
        if(c in 'Y,y'):
            spoints=self.getSPoints()
        else:
            spoints=0
        return spoints



class Student(Person,Sports):
    def __init__(self,name,age,id,sem,m1,m2):
        super().__init__(name,age)
        self.id=id
        self.sem=sem
        self.m1=m1
        self.m2=m2

    def getTotal(self):
        self.total=self.m1+self.m2+self.choice()
        return self.total
    
    def getAverage(self):
        self.avg=self.total/2
        return self.avg
    
    def getDetails(self):
        print("ID: ",self.id)
        print("Name: ",self.getName())
        print("Age: ",self.age)
        print("Sem: ",self.sem)
        print("M1: ",self.m1)
        print("M2: ",self.m2)
        print("Total: ",self.getTotal())
        print("Average: ",self.getAverage())

s1=Student('Archit',18,1,4,10,20)
s1.getDetails()