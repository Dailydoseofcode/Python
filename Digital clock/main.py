from tkinter import *
from tkinter.ttk import *
from time import strftime
root= Tk()
root.title("Clock")
def time():
    #24h format
    #string = strftime("%H:%M:%S %p")
    #12h format
    string = strftime("%I:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)
label=Label(root,font=("ds-digital",80),background="black", foreground="cyan")
label.pack(anchor="center")
time()
mainloop()