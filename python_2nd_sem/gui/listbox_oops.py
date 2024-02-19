import tkinter as tk

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(master, font=("comicsansms", 15, "bold"), bg="yellow", fg="black")
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add Task", font=("Arial", 8, "bold"), command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.task_listbox = tk.Listbox(master, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.delete_button = tk.Button(master, text="Delete Task", font=("comicsansms", 13, "bold"), command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5)

        self.delete_all_button = tk.Button(master, text="Delete All", font=("comicsansms", 13, "bold"), command=self.delete_all)
        self.delete_all_button.grid(row=2, column=1, padx=10, pady=10, ipadx=5, ipady=5)

        self.undo_button = tk.Button(master, text="Undo", font=("comicsansms", 13, "bold"), command=self.undo_delete)
        self.undo_button.grid(row=2, column=2, padx=10, pady=10, ipadx=5, ipady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        index = self.task_listbox.curselection()
        val = self.task_listbox.get(index)
        self.append([index,val])
        self.task_listbox.delete(index)

    def delete_all(self):
        self.task_listbox.delete(0, tk.END)

    def undo_delete(self):
        if self.tasks:
            self.tasks.pop()
            self.task_listbox.delete(tk.END)

root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()
