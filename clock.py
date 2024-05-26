from tkinter import *
from time import *
def update():
    time_st=strftime("%I:%M:%S %p")
    tlabel.config(text=time_st)
    day_st=strftime("%A")
    daylabel.config(text=day_st)
    date_st=strftime("%d %B, %Y")
    dlabel.config(text=date_st)
    window.after(1000,update)

window=Tk()

tlabel=Label(window,font=("Times New Roman",50),fg='red',bg="black")
tlabel.pack()
daylabel=Label(window,font=("Arial",40),fg='red')
daylabel.pack()
dlabel=Label(window,font=("Arial",30),fg="black")
dlabel.pack()

update()

window.mainloop()
