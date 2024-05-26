from tkinter import *

window=Tk()
title=Label(window,text="Details:",font=("Arial",20))
title.grid(row=0,column=0,columnspan=2)
fnlabel=Label(window,text="First Name:",bg="black",fg="red",width=20).grid(row=1,column=0)
fnentry=Entry(window).grid(row=1,column=1)
lnlabel=Label(window,text="Last Name:",bg="red",fg="black",width=20).grid(row=2,column=0)
lnentry=Entry(window).grid(row=2,column=1)
emaillabel=Label(window,text="Email:",bg="black",fg="red",width=20).grid(row=3,column=0)
email=Entry(window).grid(row=3,column=1)
button=Button(window,text="Submit",bg="black",fg="red").grid(row=4,column=0,columnspan=2)
window.mainloop()
