from cProfile import label
import string
from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title("Clock Using Python")
def time():
    string = strftime('%I:%M:%S %p')
    label.config(text= string)
    label.after(1000,time)
label = Label(root,font = ("ds-digital",80),background="grey",foreground = "purple")
label.pack(anchor='center')
time()
mainloop()