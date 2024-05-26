from tkinter import *
from tkinter.ttk import *
import time
def download():
    GB=100
    download=0
    speed=1
    while(download<GB):
        time.sleep(0.05)
        bar["value"]+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+'/'+str(GB)+" GB commpleted")
        window.update_idletasks()


window=Tk()
percent =StringVar()
text=StringVar()
bar =Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)
percentlabel=Label(window,textvariable=percent).pack()
textlabel=Label(window,textvariable=text).pack()
button=Button(window,text="Download",command=download)
button.pack()
window.mainloop()
