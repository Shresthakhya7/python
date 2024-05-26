from tkinter import *
def submit():
    movie=[]
    for index in listbox.curselection():
        movie.insert(index,listbox.get(index))
    print("watched movie=")
    for index in movie:
        print(index)
def add():
    listbox.insert(listbox.size(),ebox.get())
    listbox.config(height=listbox.size())
def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())
shrestha=Tk()

listbox=Listbox(shrestha,font=("arial",20),width=20,bg="black",
                fg="red",selectmode=MULTIPLE)
listbox.pack()
listbox.insert(1,"Salaar")
listbox.insert(2,"KGF")
listbox.insert(3,"Bahubali")
listbox.insert(4,"HI Nanna")
listbox.insert(5,"Sita Ramam")

listbox.config(height=listbox.size())

ebox=Entry(shrestha)
ebox.pack()

abutton=Button(shrestha,text="add",command=add)
abutton.pack()
sbutton=Button(shrestha,text="submit",command=submit)
sbutton.pack()
delbutton=Button(shrestha,text="delete",command=delete)
delbutton.pack()

shrestha.mainloop()
