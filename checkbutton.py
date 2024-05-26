from tkinter import *
def display():
    if (x.get()==1):
        print("Agree")
    else:
        print("Dont agree")
window=Tk()

x=IntVar()
checkbox=Checkbutton(window,text="just check it",
                     variable=x,
                     onvalue=1,
                     offvalue=0,command=display,
                     fg="red",bg="black",
                     font=("Times New Roman",50),
                     activebackground="red",
                     activeforeground="black")
checkbox.pack()
window.mainloop()
