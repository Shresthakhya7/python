from tkinter import *

window=Tk()

frame=Frame(window,bg="black",bd=5,relief=SUNKEN)
frame.pack()
Button(frame, text="W", width=3, font=("Alias", 20),bg="red").pack(side=TOP)
Button(frame, text="A", width=3, font=("Alias", 20),bg="red").pack(side=LEFT)
Button(frame, text="S", width=3, font=("Alias", 20),bg="red").pack(side=LEFT)
Button(frame, text="D", width=3, font=("Alias", 20),bg="red").pack(side=LEFT)
window.mainloop()
