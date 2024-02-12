import tkinter as tk

def display_greeting():
    name = input_field.get()
    greeting_label.config(text=f"Hello, {name}!")

window = tk.Tk()
window.title("Welcome to Sanskar's Name App")
window.minsize(width=500, height=400)

# Label
prompt_label = tk.Label(
    window,
    text="Please enter your name:",
    font=("Arial", 24, "bold")
)
prompt_label.place(x=50, y=50)

# Entry
input_field = tk.Entry(window, width=25)
input_field.pack(side="left")


# Button
greet_button = tk.Button(
    window,
    text="Click me",
    command=display_greeting
)
greet_button.place(x=125, y=100)  


greeting_label = tk.Label(
    window,
    text="",
    font=("Arial", 18)
)
greeting_label.place(x=50, y=150)

window.mainloop()
