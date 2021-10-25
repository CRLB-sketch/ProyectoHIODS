# Vista

import tkinter as tk
# from tkinter import ttk
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image

class View(tk.Tk):
    def __init__(self, controller):
        #############################################################
        super().__init__()

        self.title("Helper Ingenious")

        self.controller = controller
        
        self.geometry("780x560")

        # self.state('zoomed')
        
        self._page1()

        ##########################################################
        # self.rowconfigure(0, weight=1)
        # self.columnconfigure(0, weight=1)

        # self.frame1 = Frame(self)
        # self.frame2 = Frame(self)

        # # for frame in (self.frame1, self.frame2):
        # #     frame.grid(row=0,column=0,stick="nsew")

        # #==================Frame 1 code
        # frame1_title = Label(self.frame1, text='Page 1', font='times 35', bg='red')
        # frame1_title.pack(fill='both', expand=True)

        # frame1_btn = Button(self.frame1, text='Enter',command=lambda:self._show_frame(self.frame2))
        # frame1_btn.pack(fill='x', ipady=15)

        # #==================Frame 2 code
        # frame2_title=  Label(self.frame2, text='Page 2', font='times 35', bg='yellow')
        # frame2_title.pack(fill='both', expand=True)

        # frame2_btn = Button(self.frame2, text='Enter',command=lambda:self._show_frame(self.frame1))
        # frame2_btn.pack(fill='x', ipady=15)  

        # self._show_frame(self.frame1)

      
    def main(self):        
        self.mainloop()

    def _show_frame(frame):
        frame.tkraise()

    def _page1(self):
        # Set background
        self.filename = PhotoImage(file="images//1.png")
        background_label = Label(self, image=self.filename)
        background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        
        # Set Buttons
        def thing1():
            print("Necesitas apoyo")

        def thing2():
            print("Quiero apoyar")

        def thing3():
            print("Quiero ser voluntariado")

        # Para el boton 3
        # my_pic = Image.open("images//planet_3.png")
        # # resized = my_pic.resize((300, 225), Image.ANTIALIAS)

        self.button3 = PhotoImage(file="images//planet_3.png")
        # img1_label = Label(image=self.button1)
        my_button3 = Button(self, image=self.button3, command=thing3, relief="raised", borderwidth=5, width=150, height=150)
        my_button3.pack(pady=10)
        # my_button3.config(compound=)
        # my_label3 = Label(self, text="")
        # my_label3.pack(pady=200)

        # my_button3.grid(row=0,column=0,pady=5) ##########################

        # # Para el boton 1
        self.button1 = PhotoImage(file="images//planet_1.png")
        my_button1 = Button(self, image=self.button1, command=thing1, relief="raised", borderwidth=3, width=150, height=150)
        my_button1.pack(pady=10)

        # # Para el boton 1
        self.button2 = PhotoImage(file="images//planet_2.png")
        my_button2 = Button(self, image=self.button2, command=thing2, relief="raised", borderwidth=3, width=150, height=150)
        my_button2.pack(pady=10)

        # my_label1 = Label(self, text="")
        # my_label1.pack(pady=20)

        # my_button1.grid(row=1,column=0,pady=5) ##########################