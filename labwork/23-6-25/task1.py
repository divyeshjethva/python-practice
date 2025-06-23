class a:
    def fun1(self):
        print("method 1")

class b(a):
    def fun1(self):
        super().fun1()
        
        print("method 2")

class c(b):
    def fun1(self):
        super().fun1()
        print("method 4")
        
obj = c()
obj.fun1()