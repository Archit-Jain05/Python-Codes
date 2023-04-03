class student:
    
    def getStudent(self):
        print("ID: ",self.ID)
        print("Name: ",self.name)
        print("Discipline: ",self.dis)
        print("Marks: ",self.marks)

    def setStudent(self):
        print("Enter ID:")
        self.ID=int(input())
        print("Enter name:")
        self.name=input()
        print("Enter Discipline:")
        self.dis=input()
        i=1
        self.marks=[]
        print("Enter number of subjects to enter:")
        self.n=int(input())
        for i in range(1,self.n+1):
            print("Enter Marks ",i ,": ")
            a=int(input())
            self.marks.append(a)
        
    def avg(self):
        print("")

        
print("Enter the number of students to enter:")
num=int(input())
i=0
stu=[]
for i in range(0,num):
    stu.append(i)
    stu[i]=student()
    stu[i].setStudent()
i=0
for i in range(0,num):
    stu[i].getStudent()
