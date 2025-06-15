d = {}
class student:
    def set_name(self,name):
        self.name = name
        d[name] = {}
    def show_name(self):
        print("NAME :", self.name)

class roll(student):
    def set_roll(self, roll):
        self.roll = roll
    def show_roll(self):
        self.show_name()
        d[self.name] = {"roll":self.roll}
        print("ROLL NO :", self.roll)

class marks(roll):
    def set_marks(self,marks):
        self.marks = marks
    def show_marks(self):
        self.show_roll()
        d[self.name] = {"roll":self.roll,"marks":self.marks}
        print("MARKS :", self.marks)
        
    def print_dic(self):
    
        for i,j in d.items():
            print(i,":")
            for k,v in j.items():
                print("     ",k,":",v)
            print("==========================")


obj = marks()
obj.set_name("divyesh")
obj.set_roll(78)
obj.set_marks(100)
obj.show_marks()
obj.print_dic()