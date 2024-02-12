import tkinter as tk

def increment_action():
    value.set(value.get() + 1)
    if value.get() >= 10:
        label.config(fg='red')
    else: 
        label.config(fg='green')

def decrement_action():
    value.set(value.get() - 1)
    
    
    if value.get() >= 10:
        label.config(fg='red')
    else:
        label.config(fg='green')

#global


window = tk.Tk()
window.geometry('300x300')
window.title('Counter App')
window.minsize(200, 100)
window.maxsize(300, 200)

value = tk.IntVar(value=0)

tk.Label(window, text="Welcome to sanskar's Counter App").pack()
label = tk.Label(window, textvariable=value, font=('arial', 24),fg= "green")
label.pack()

button_increment = tk.Button(window, text='Increment', command=increment_action)
button_increment.place(x=150,y=230)
button_increment.pack( padx=8, pady=8)

button_decrement = tk.Button(window, text='Decrement', command=decrement_action)
button_decrement.place(x=180,y=130)
button_decrement.pack( padx=8, pady=8)

window.mainloop()
