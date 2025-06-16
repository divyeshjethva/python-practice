# hybrid

class a:
    def fun1(self):
        print("class a")

class b(a):
    def fun2(self):
        print("class b")

class c:
    def fun3(self):
        print("class c")

class d(b,c):
    def fun4(self):
        print("class d is child class")
        
obj = d()

obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()