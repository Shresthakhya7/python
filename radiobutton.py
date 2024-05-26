from tkinter import *

superhero=["batman","spiderman","ironman"]
def choose():
    if(x.get()==0):
        print("choose batman")
    elif(x.get()==1):
        print("choose spiderman")
    else:
        print("choose ironman")
shrestha =Tk()
shrestha.title("Hero")

x=IntVar()
for index in range(len(superhero)):
    radio=Radiobutton(shrestha,text=superhero[index],
                  variable=x,
                      value=index,
                      padx=25,
                      width=10,
                      indicatoron=0,
                      command=choose,
                      font=("Arial",50),
                      fg="Red",
                      bg="black",)
    radio.pack(anchor=W)

shrestha.mainloop()
