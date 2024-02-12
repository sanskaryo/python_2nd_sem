import tkinter as tk
from tkinter import messagebox


class app:
    def __init__(self,mainwindow):
        self.mainwindow = mainwindow
        self.mainwindow.geometry('400x200')
        self.mainwindow.title('celcius to farenheit')
        self.mainwindow.minsize(100, 200)
        
        
        
        
        
        
        self.celsius_label = tk.Label(root, text= " Enter the temperature in celsius" , font=("Arial", 24, "bold") )
        
        self.celsius_label.pack()
        
        
        
        
        
        
        
        
        
root = tk.Tk()
exc = app(root)
root.mainloop()