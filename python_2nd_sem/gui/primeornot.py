from tkinter import *

window = Tk()
window.title("Welcome to sankhuz app")
window.minsize(width=500, height=350)

# label2
label2 = Label(text="Enter the number of your choice", font=("Arial", 15, "italic"))
label2.place(x=220, y=50)

# label1
my_label = Label(text="Result will be displayed here", font=("Arial", 24, "bold"))
my_label.place(x=150, y=100)
my_label.config(padx=50, pady=50)

# primeno
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# button
def button_clicked():
    num = int(input.get())
    if is_prime(num):
        my_label.config(text=f"{num} is a prime number")
    else:
        my_label.config(text=f"{num} is not a prime number")

button = Button(text="Check Prime", command=button_clicked)
button.pack()

# entry
input = Entry(width=15)
input.pack()

window.mainloop()
