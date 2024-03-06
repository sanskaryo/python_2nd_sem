import tkinter as tk

from tkinter import messagebox


class tic_tac_toe:
    def __init__(self, root):
        self.gamestri = "X"
        self.root = root
        self.bt1 = tk.Button(root)
        self.bt1.grid(row=0, column=0, ipadx=40, ipady=40)
        self.bt1.config(command=lambda: self.write_to_it(self.bt1))
        self.bt2 = tk.Button(root)
        self.bt2.grid(row=0, column=1, ipadx=40, ipady=40)
        self.bt3 = tk.Button(root)
        self.bt2.config(command=lambda: self.write_to_it(self.bt2))
        self.bt3.grid(row=0, column=2, ipadx=40, ipady=40)
        self.bt3.config(command=lambda: self.write_to_it(self.bt3))

        self.bt4 = tk.Button(root)
        self.bt4.grid(row=1, column=0, ipadx=40, ipady=40)
        self.bt4.config(command=lambda: self.write_to_it(self.bt4))
        self.bt5 = tk.Button(root)
        self.bt5.grid(row=1, column=1, ipadx=40, ipady=40)
        self.bt5.config(command=lambda: self.write_to_it(self.bt5))
        self.bt6 = tk.Button(root)
        self.bt6.grid(row=1, column=2, ipadx=40, ipady=40)
        self.bt6.config(command=lambda: self.write_to_it(self.bt6))

        self.bt7 = tk.Button(root)
        self.bt7.grid(row=2, column=0, ipadx=40, ipady=40)
        self.bt7.config(command=lambda: self.write_to_it(self.bt7))
        self.bt8 = tk.Button(root)
        self.bt8.grid(row=2, column=1, ipadx=40, ipady=40)
        self.bt8.config(command=lambda: self.write_to_it(self.bt8))
        self.bt9 = tk.Button(root)
        self.bt9.grid(row=2, column=2, ipadx=40, ipady=40)
        self.bt9.config(command=lambda: self.write_to_it(self.bt9))

        root.mainloop()

    def write_to_it(self, bt):
        if self.gamestri == "X":
            bt.config(text=self.gamestri)
            self.gamestri = "O"
        else:
            bt.config(text=self.gamestri)
            self.gamestri = "X"
        self.checker()

    def reset(self):
        self.gamestri = "X"

        self.bt1.config(text="")
        self.bt2.config(text="")
        self.bt3.config(text="")
        self.bt4.config(text="")
        self.bt5.config(text="")
        self.bt6.config(text="")
        self.bt7.config(text="")
        self.bt8.config(text="")
        self.bt9.config(text="")

    def checker(self):
        # print(self.bt1.cget('text'))
        if (self.bt1.cget('text') == "X" and self.bt2.cget('text')=="X" and self.bt3.cget('text')=="X"):
            messagebox.showinfo("Winner of the Game", "X Wins the Game")
            ans = messagebox.askyesno("Retry", "Do You want to Retry?")
            if ans== True:
                self.reset()
            else:
                self.root.destroy()
        elif (self.bt1.cget('text') == "O" and self.bt2.cget('text')=="O" and self.bt3.cget('text')=="O"):
            messagebox.showinfo("Winner of the Game", "O Wins the Game")
            ans = messagebox.askyesno("Retry", "Do You want to Retry?")
            if ans== True:
                self.reset()
            else:
                self.root.destroy()
        elif (self.bt4.cget('text') == "X" and self.bt5.cget('text')=="X" and self.bt6.cget('text')=="X"):
            messagebox.showinfo("Winner of the Game", "X Wins the Game")
            ans = messagebox.askyesno("Retry", "Do You want to Retry?")
            if ans== True:
                self.reset()
            else:
                self.root.destroy()
        elif (self.bt4.cget('text') == "O" and self.bt5.cget('text')=="O" and self.bt6.cget('text')=="O"):
            messagebox.showinfo("Winner of the Game", "O Wins the Game")
            ans = messagebox.askyesno("Retry", "Do You want to Retry?")
            if ans== True:
                self.reset()
            else:
                self.root.destroy()
        elif (self.bt7.cget('text') == "X" and self.bt8.cget('text')=="X" and self.bt9.cget('text')=="X"):
            messagebox.showinfo("Winner of the Game", "X Wins the Game")
            ans = messagebox.askyesno("Retry", "Do You want to Retry?")
            if ans== True:
                self.reset()
            else:
                self.root.destroy()
        elif (self.bt7.cget('text') == "O" and self.bt8.cget('text')=="O" and self.bt9.cget('text')=="O"):
            messagebox.showinfo("Winner of the Game", "O Wins the Game")
            ans = messagebox.askyesno("Retry", "Do You want to Retry?")
            if ans== True:
                self.reset()
            else:
                self.root.destroy()
        elif (self.bt1.cget('text') == "X" and self.bt4.cget('text')=="X" and self.bt7.cget('text')=="X"):
            messagebox.showinfo("Winner of the Game", "X Wins the Game")
            ans = messagebox.askyesno("Retry", "Do You want to Retry?")
            if ans== True:
                self.reset()
            else:
                self.root.destroy()
        elif (self.bt1.cget('text') == "O" and self.bt4.cget('text')=="O" and self.bt7.cget('text')=="O"):
            messagebox.showinfo("Winner of the Game", "O Wins the Game")
            ans = messagebox.askyesno("Retry", "Do You want to Retry?")
            if ans== True:
                self.reset()
            else:
                self.root.destroy()
        elif (self.bt2.cget('text') == "X" and self.bt5.cget('text')=="X" and self.bt8.cget('text')=="X"):
            messagebox.showinfo("Winner of the Game", "X Wins the Game")
            ans = messagebox.askyesno("Retry", "Do You want to Retry?")
            if ans== True:
                self.reset()
            else:
                self.root.destroy()
        elif (self.bt2.cget('text') == "O" and self.bt5.cget('text')=="O" and self.bt8.cget('text')=="O"):
            messagebox.showinfo("Winner of the Game", "O Wins the Game")
            ans = messagebox.askyesno("Retry", "Do You want to Retry?")
            if ans== True:
                self.reset()
            else:
                self.root.destroy()
        elif (self.bt3.cget('text') == "X" and self.bt6.cget('text')=="X" and self.bt9.cget('text')=="X"):
            messagebox.showinfo("Winner of the Game", "X Wins the Game")
            ans = messagebox.askyesno("Retry", "Do You want to Retry?")
            if ans== True:
                self.reset()
            else:
                self.root.destroy()
        elif (self.bt3.cget('text') == "O" and self.bt6.cget('text')=="O" and self.bt9.cget('text')=="O"):
            messagebox.showinfo("Winner of the Game", "O Wins the Game")
            ans = messagebox.askyesno("Retry", "Do You want to Retry?")
            if ans== True:
                self.reset()
            else:
                self.root.destroy()
        elif (self.bt1.cget('text') == "X" and self.bt5.cget('text')=="X" and self.bt9.cget('text')=="X"):
            messagebox.showinfo("Winner of the Game", "X Wins the Game")
            ans = messagebox.askyesno("Retry", "Do You want to Retry?")
            if ans== True:
                self.reset()
            else:
                self.root.destroy()
        elif (self.bt1.cget('text') == "O" and self.bt5.cget('text')=="O" and self.bt9.cget('text')=="O"):
            messagebox.showinfo("Winner of the Game", "O Wins the Game")
            ans = messagebox.askyesno("Retry", "Do You want to Retry?")
            if ans== True:
                self.reset()
            else:
                self.root.destroy()
        elif (self.bt3.cget('text') == "X" and self.bt5.cget('text')=="X" and self.bt7.cget('text')=="X"):
            messagebox.showinfo("Winner of the Game", "X Wins the Game")
            ans = messagebox.askyesno("Retry", "Do You want to Retry?")
            if ans== True:
                self.reset()
            else:
                self.root.destroy()
        elif (self.bt3.cget('text') == "O" and self.bt5.cget('text')=="O" and self.bt7.cget('text')=="O"):
            messagebox.showinfo("Winner of the Game", "O Wins the Game")
            ans = messagebox.askyesno("Retry", "Do You want to Retry?")
            if ans== True:
                self.reset()
            else:
                self.root.destroy()
        elif (self.bt1.cget("text") != "" and self.bt2.cget("text") != "" and
               self.bt3.cget("text") != "" and self.bt4.cget("text") != "" and
                 self.bt5.cget("text") != "" and self.bt6.cget("text") != "" and
                   self.bt7.cget("text") != "" and self.bt8.cget("text") != "" and
                     self.bt9.cget("text") != ""):
            messagebox.showinfo("Winner of the Game", "Game is Tie")
            ans = messagebox.askyesno("Retry", "Do You want to Retry?")
            if ans== True:
                self.reset()
            else:
                self.root.destroy()
              

    

root = tk.Tk()
a = tic_tac_toe(root)