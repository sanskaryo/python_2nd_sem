import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def action():
    
    num1 = eval(entry1.get())
    num2 = eval(entry2.get())
    
    data = num1 + num2
    messagebox.showinfo("result", data)

tk.Label(root, text="enter the first number").grid(row=0,column=0,padx=5,pady=5)
tk.Label(root, text="enter the second number").grid(row=1,column=0,padx=5,pady=5)

entry1 = tk.Entry(root)
entry1.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W)

entry2 = tk.Entry(root)
entry2.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)

#button

bt1 = tk.Button(root,text="calculate",command=action)
bt1.grid(row=2,column=2,columnspan=2)



root.mainloop()