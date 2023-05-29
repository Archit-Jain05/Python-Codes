class MyException(Exception):
    def __init__(self,msg):
        self.msg=msg

    def __str__(self):
        return f'CustomException: {self.msg}'



raise MyException("Exception 1")       