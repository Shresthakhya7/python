from tkinter import *
from tkinter import messagebox
count=0
def click():
    print("hello.txt "+ebox.get())
def delete():
    ebox.delete(0,END)
def back():
    ebox.delete(len(ebox.get())-1,END)

window=Tk()
window.geometry("1000x500")
window.title("shrestha")

icon= PhotoImage(file='logo1.png')
window.iconphoto(True,icon)
window.config(background="grey")
label=Label(window,text="Shreejan Khya Shrestha",
            font=('Arial',20),fg="red",bg="black",
            relief=RAISED,bd=10)
label.pack()
ebox=Entry(window,font=("Arial",50))
ebox.pack(side=LEFT)
button=Button(window,text="Click me",command=click)
button.pack(side=RIGHT)
dbutton=Button(window,text="Delete",command=delete)
dbutton.pack(side=RIGHT)
bbutton=Button(window,text="BAck",command=back)
bbutton.pack(side=RIGHT)
window.mainloop()
