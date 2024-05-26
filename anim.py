from tkinter import *
import time
from Ball import *

window=Tk()
WIDTH=500
HEIGHT=500
canvas=Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()
vball=Ball(canvas,0,0,100,3,1,"white")
tball=Ball(canvas,5,5,50,4,3,"yellow")
basketball=Ball(canvas,50,50,150,15,10,"orange")

while True:
    
    vball.move()
    tball.move()
    basketball.move()

    window.update()
    time.sleep(0.00001)

window.mainloop()
