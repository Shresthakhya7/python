from tkinter import *
def save():
    print("file saved")
def openf():
    print("file open")
def cut():
    print("file cut")
def copy():
    print(("file copied"))
def paste():
    print("file pasted")
window =Tk()
window.title("Menubar")
menubar=Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0,font=("Arial",20),bg="black",fg="red")
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Open",command=openf)
filemenu.add_command(label="Save",command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit)


editmenu = Menu(menubar,tearoff=0,font=("Arial",20),bg="black",fg="red")
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_separator()
editmenu.add_command(label="Paste",command=paste)

window.mainloop()


