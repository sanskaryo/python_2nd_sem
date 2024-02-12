import tkinter

root = tkinter.Tk()
root.title("my first gui program with py and tkinter")
root.minsize(width=500, height=300)

my_label = tkinter.Label(text="Hello Duniya", font=("Arial", 24, "italic"))
my_label.pack(side="left")


root.mainloop()
