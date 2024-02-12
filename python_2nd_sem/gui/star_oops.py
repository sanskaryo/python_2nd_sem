import tkinter as tk

class app:
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.mainwindow.geometry('400x200')
        self.mainwindow.title('star pattern')
        self.mainwindow.minsize(100, 200)

        tk.Label(mainwindow, text="Enter a number: ").pack()

        self.name_entry = tk.Entry(mainwindow)
        self.name_entry.pack()

        self.click = tk.Button(mainwindow, text="Check", command=self.action)
        self.click.pack()
        self.outlabel = tk.Label(mainwindow, text="")
        self.outlabel.pack()

    def action(self):
        data = int(self.name_entry.get())
        st = ''
        for i in range(1, data):
            for j in range(i):
                st += "*"
            st += "\n"
        self.outlabel.config(text=st)

# Main code
root = tk.Tk()
exc = app(root)
root.mainloop()
