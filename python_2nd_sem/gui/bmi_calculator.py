from tkinter import *
from tkinter import messagebox



window = Tk()
window.title("Bmi calculator")
window.config(padx=50, pady=50)

Label1 = Label(text="Calculate BMI - Become Fit",font="Arial",padx=10,pady=10)
Label1.grid(column=0,row=0)


#function


def calculate_bmi():
    height = int(entry1.get())
    weight = int(entry2.get())
    bmi = weight / (height / 100) ** 2
    messagebox.showinfo(title="BMI", message=f"Your BMI is {round(bmi,2)}")



label1 = Label(text="Height (cm)")
label1.grid(column=0, row=1)

label2 = Label(text="Weight (kg)")
label2.grid(column=0, row=2)

entry1 = Entry(width=10)
entry1.grid(column=1, row=1)

entry2 = Entry(width=10)
entry2.grid(column=1, row=2)

button1 = Button(text="Calculate", command=calculate_bmi)
button1.grid(column=1, row=3)


window.mainloop()
