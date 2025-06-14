class first:
    def fun1(self):
        print("hello world")
    def fun2(self):
        print("fun 2 !!")

class second(first):
    def fun3(self):
        print("second class fun 1")
    def fun4(self):
        print("second class fun 2")
        
class third(second):
    def fun5(self):
        print("second class fun 5")
    def fun6(self):
        print("second class fun 6")
    
obj = third()
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()
obj.fun5()
obj.fun6()