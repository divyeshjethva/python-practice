# from tkinter import *

# x = 50
# y = 40
# root = Tk()

# root.geometry("1200x600")
# root.title("All products ")
# root.configure(bg="grey")

# photo = PhotoImage(file='photo.png')
# Frame(root,height=210,width=160,borderwidth=2,relief='solid').place(x=x,y=y)

# label = Label(root, image=photo)
# label.pack()

# root.mainloop()



from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Show Image")
root.geometry("400x400")

image = Image.open(rf"C:\Users\ADMIN\Desktop\backend developer\python-practice\labwork\3-7-25\gg.jpg")
image = image.resize((300, 300)) 
photo = ImageTk.PhotoImage(image)

label = Label(root, image=photo)
label.pack()

root.mainloop()
