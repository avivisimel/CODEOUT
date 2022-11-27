import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title("CODEOUT launcher")

class Button:

    row = 0
    column = 0
    def __init__(self, text, func, arg, image=""):
        if image!= "":
            image = tk.PhotoImage(file=image)
        root.rowconfigure(Button.row, weight=1, minsize=40)
        root.rowconfigure(Button.column, weight=1, minsize=40)