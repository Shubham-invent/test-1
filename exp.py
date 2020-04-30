from tkinter import *
from PIL import ImageTk,Image

window=Tk()

window.title("Hello world")
window.configure(bg="Sky Blue")
#f1 =Frame(window)
#sb = Scrollbar(top)  
#sb.pack(side = RIGHT, fill = Y)
#mylist = Listbox(top, yscrollcommand = sb.set )


l2=ImageTk.PhotoImage(Image.open('test/pic1.jpg'))
l1=Label(window,image=l2)
l1.grid(row=0,column=0)
mylabel=Label(window,text="first page!! ",font=("MV Boli",40),foreground="red",bg="sky blue")
mylabel.grid(row=0,column=1)
window.mainloop()


