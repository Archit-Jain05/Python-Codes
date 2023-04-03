class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
class Employee(Person):
    def __init__(self,name,age,code,exp,bsal):
        super().__init__(name,age)
        self.code=code
        self.exp=exp
        self.bsal=bsal

    def getDetails(self):
        print(self.getName())
        print(self.getAge())
        print(self.code)
        print(self.exp)
        print(self.grossSal())
    
    def grossSal(self):
        gsal=self.bsal+self.bsal*0.37+self.bsal*0.78+self.bsal*0.06
        return gsal


e1=Employee("Archit",18,10,12,1000)
e1.getDetails()
