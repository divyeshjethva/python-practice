# multipel

class A:
    def fun1(self):
        print("method 1")

class B:
    def fun2(self):
        print("method 2")

class C(A,B):
    def fun3(self):
        print("method 3")

obj = C()
obj.fun3()
obj.fun1()
obj.fun2()


