import tkinter as tk
from tkinter import messagebox
class bmi:
    def __init__(self, mainwindow):
        mainwindow.geometry("500x400")
        mainwindow.title("BMI CALCULATOR")


        tk.Label(mainwindow,text="Calculate Your Body Mass Index",font=("Arial",15,"bold"),fg="black",padx=10,pady=10).grid(row=0,column=3)


        tk.Label(mainwindow,text="Weight",font=("comicsansms",15,"bold"),fg="black",padx=10,pady=10).grid(row=1,column=3)
        self.weight=tk.Entry(root,font=("comicsansms",15,"bold"),bg="yellow",fg="black")
        self.weight.grid(row=2,column=3)

        tk.Label(mainwindow,text="Height",font=("comicsansms",15,"bold"),fg="black",padx=10,pady=10).grid(row=3,column=3)
        self.height=tk.Entry(root,font=("comicsansms",15,"bold"),bg="yellow",fg="black")
        self.height.grid(row=4,column=3)

        tk.Button(mainwindow,text="Check",font=("comicsansms",15,"bold"),bg="pink",fg="black",command=self.bmi_calc).grid(row=5,column=2)


    def bmi_calc(self):
        weight=int(self.weight.get())
        height=int(self.height.get())
        bmi=weight/((height/100)**2)
        messagebox.showinfo('BMI', f"Your BMI is {round(bmi,2)}")





root=tk.Tk()
exe=bmi(root)
root.mainloop()
