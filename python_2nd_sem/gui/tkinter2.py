from tkinter import *

window = Tk()

window.title("Welcome to sankhuz app")
window.minsize(width=500, height=350)

#label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()
my_label.place(x=150, y=100)
my_label.config(padx=50, pady=50)

#button

def button_clicked():
    print("I got clicked")
    my_label.config(text= input.get())

button = Button(text="Click me", command=button_clicked)
button.pack()

#entry

input = Entry(width=15)
input.pack()
input.get()


window.mainloop()