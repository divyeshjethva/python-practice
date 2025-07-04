from tkinter import *
from PIL import Image, ImageTk
l = [599,565,233,54,123,455]

root = Tk()

root.geometry("1200x600")
root.title("All products ")
root.configure(bg="grey")

def product(path,i,x,y):
    Frame(root,height=220,width=160,borderwidth=2,relief='solid').place(x=x,y=y)

    image = Image.open(path)
    image = image.resize((152,145)) 
    photo = ImageTk.PhotoImage(image)

    label = Label(root, image=photo)
    label.image = photo
    label.place(x=x+2,y=y+2)
    
    Label(root,text=f"$ {i}",font=('Arial',12)).place(x=x+5,y=y+150)
    
    Button(root,text="Add to card",bg='green',fg='white',font=('Arial',10,'bold'),width=16).place(x=x+10,y=y+187)

path = rf"C:\Users\ADMIN\Desktop\backend developer\python-practice\labwork\3-7-25\gg.jpg"

x = 50 
y = 40
for i in l:
    product(path,i,x,y)
    x = x + 180
    
root.mainloop()

