class first:
    def fun1(self):
        print("hello world")
    
    def fun2(self):
        print("fun 2 !!")

class second:
    def fun1(self):
        print("second class fun 1")
    
obj = first()
obj1 = second()
obj1.fun1()
obj.fun1()
obj.fun2()