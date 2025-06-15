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

for i in range(2):
    name_d = input("Enter name :")
    roll_d = int(input("Enter roll no. :"))
    marks_d = int(input("Enter marks :"))
    
    obj.set_name(name_d)
    obj.set_roll(roll_d)
    obj.set_marks(marks_d)
    print("------------------------")
    
obj.show_marks()
obj.print_dic()
