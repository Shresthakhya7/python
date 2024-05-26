from tkinter import *
def submit():
    print("number is "+str(scale.get()))
shrestha =Tk()

scale=Scale(shrestha,from_=0,to_=100,
            length=500,
            orient=VERTICAL,
            tickinterval=10,#showvalue=0
            resolution=10,
            troughcolor="skyblue",
            fg="red",bg="black")
#scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

b=Button(shrestha,text="submit",command=submit,font=("Constania",20),
         fg="red",bg="black")
b.pack()
shrestha.mainloop()
