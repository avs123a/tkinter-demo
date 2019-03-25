from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog

window = Tk()
window.title("Welcome to Repl.it")
window.geometry('150x300')

lbl = Label(window, text="Basic demos")
lbl.grid(column=1, row=0)

def color_click():
    result = colorchooser.askcolor(color="#6A9662", title = "Select Color") 
    print(result)

def input_btn_click():
    window2 = Tk()
    window2.title("INPUTS")
    Label(window2, text = "Text").grid(row = 0)
    Entry(window2).grid(row = 0, column = 1)

def query_click():
    messagebox.askquestion("Question", "It is working?")

def open_file():
    fname= filedialog.askopenfilename() 
    print(fname)

def err_click():
    messagebox.showerror("Error", "Testing error alert!")

def close_wnd():
    window.destroy

btn1 = Button(window, text="Color", command=color_click)
btn1.grid(column=1, row=1)

btn2 = Button(window, text="Query", command=query_click)
btn2.grid(column=1, row=2)

btn3 = Button(window, text="Input", command=input_btn_click)
btn3.grid(column=1, row=3)

btn4 = Button(window, text="Open", command=open_file)
btn4.grid(column=1, row=4)

btn5 = Button(window, text="Error", command=err_click)
btn5.grid(column=1, row=5)

btn6 = Button(window, text="Quit", command=close_wnd)
btn6.grid(column=1, row=6)

window.mainloop()