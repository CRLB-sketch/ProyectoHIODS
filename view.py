# Vista

import tkinter as tk
# from tkinter import ttk
from tkinter import *
from tkinter import messagebox

class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()

        self.title("Helper Ingenious")

        self.controller = controller
        
        self.geometry("780x560")
        
        self._page1()

    def main(self):
        self.mainloop()

    def _page1(self):
        self.filename = PhotoImage(file="images//testing_png.png")
        background_label = Label(self, image=self.filename)
        background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        