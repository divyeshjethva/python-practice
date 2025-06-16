# hirachi

class a:
    def fun1(self):
        print("method 1")
        
class b(a):
    def fun2(self):
        print("method 2")

class c(a):
    def fun3(self):
        print("method 3")

obj1 = b()

obj1.fun1()
obj1.fun2()


obj2 = c()
obj2.fun1()
obj2.fun3()