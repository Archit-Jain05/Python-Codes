class SalaryNotInRange (Exception):
    def __init__(self,salary,message="Salary not in range of (5000,15000)"):
        self.salary=salary
        self.msg=message
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.salary}->{self.msg}'

sal=int(input("Enter salary :"))
if not 5000<sal<15000:
    raise SalaryNotInRange(sal)
