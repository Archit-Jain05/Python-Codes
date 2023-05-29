class A():
    def hehe(self):
        print("HEHEHEHE")

class C():
    def huihui(self):
        print("HUIHUIHI")

class B(A,C):
    pass

b=B()
b.hehe()
b.huihui()