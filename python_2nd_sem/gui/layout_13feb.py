'''
Layout management is the process of arranging widgets on a Tkinter window in Python. 
There are three layout managers in Tkinter: pack, place, and grid. The pack() method is used to arrange widgets 
in a horizontal or vertical stack'''

'''
Layout management is the process of arranging widgets on a Tkinter window in Python. 
There are three layout managers in Tkinter: pack, place, and grid. The pack() method is used to arrange widgets 
in a horizontal or vertical stack'''


import tkinter as tk

def add_item():
    item = entry.get()
    if item:
        list_box.insert(tk.END, item)
        entry.delete(0, tk.END)

def delete_item():
    selected = list_box.curselection()
    if selected:
        list_box.delete(selected)

def delete_all_item():
    list_box.delete(0, tk.END)

root = tk.Tk()
root.title("To Do List")
root.geometry("400x300")

entry = tk.Entry(root)
entry.grid(row=0, column=0)

bt_add = tk.Button(root, text="Add Item", command=add_item)
bt_add.grid(row=0, column=1)

list_box = tk.Listbox(root,height=10,)
list_box.grid(row=1, column=0, columnspan=2)

bt_delete = tk.Button(root, text="Delete Item", command=delete_item)
bt_delete.grid(row=2, column=0)

bt_delete_all = tk.Button(root, text="Delete All Item", command=delete_all_item)
bt_delete_all.grid(row=2, column=1)

root.mainloop()
