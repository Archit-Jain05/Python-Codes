import abc

class Figure(abc.ABC):
    def area(self):
        pass


class Rectangle(Figure):
    def __init__(self,d1,d2):
        self.d1=d1
        self.d2=d2

    def area(self):
        return self.d1*self.d2
    
    def getDim(self):
        print("Length = ",self.d1)
        print("Breadth = ",self.d2)

f1=Rectangle(10,20)

print(f1.area())