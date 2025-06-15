class student:
    def set_name(self,name):
        self.name = name
    def show_name(self):
        print("NAME :", self.name)

class roll(student):
    def set_roll(self, roll):
        self.roll = roll
    def show_roll(self):
        self.show_name()
        print("ROLL NO :", self.roll)

obj = roll()
obj.set_name("divyesh")
obj.set_roll(78)
obj.show_roll()
