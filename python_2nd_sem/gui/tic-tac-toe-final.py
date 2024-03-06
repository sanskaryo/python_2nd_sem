import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class tic_tac_toe:
    def __init__(self, root):
        self.root = root
        self.root.geometry('500x500')
        self.root.title("Tic Tac Toe")

        # Frame 2
        self.frame2 = tk.Frame(root, bg="white", width=500, height=500)
        self.frame2.pack()

        self.check = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.gamestri = "X"

        file = "X.gif"  # Default image for buttons
        im = Image.open(file)
        frames = im.n_frames
        self.img_list = [ImageTk.PhotoImage(im.seek(i)) for i in range(frames)]

        self.btn = [[None, None, None] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.btn[i][j] = tk.Button(self.frame2, image=self.img_list[0], command=lambda i=i, j=j: self.write_to_it(i, j))
                self.btn[i][j].grid(row=i, column=j)

    def animation(self, count, i, j):
        self.btn[i][j].config(image=self.img_list[count])
        if count < len(self.img_list) - 1:
            self.root.after(100, lambda: self.animation(count + 1, i, j))

    def write_to_it(self, i, j):
        if self.check[i][j] == 0:
            self.check[i][j] = self.gamestri

            if self.gamestri == "X":
                self.animation(0, i, j)
            elif self.gamestri == "O":
                self.animation(0, i, j)

            self.btn[i][j].configure(state=tk.DISABLED)

            if self.check_winner():
                self.show_winner()
            elif self.check_draw():
                self.show_draw()
            else:
                self.gamestri = "O" if self.gamestri == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.check[i][0] == self.check[i][1] == self.check[i][2] != 0 or \
               self.check[0][i] == self.check[1][i] == self.check[2][i] != 0:
                return True
        if self.check[0][0] == self.check[1][1] == self.check[2][2] != 0 or \
           self.check[0][2] == self.check[1][1] == self.check[2][0] != 0:
            return True
        return False

    def check_draw(self):
        for i in self.check:
            for j in i:
                if j == 0:
                    return False
        return True

    def show_winner(self):
        winner = "X" if self.gamestri == "O" else "O"
        messagebox.showinfo("Winner of the Game", f"{winner} Wins the Game")
        self.reset()

    def show_draw(self):
        messagebox.showinfo("Draw", "It's a draw!")
        self.reset()

    def reset(self):
        for i in range(3):
            for j in range(3):
                self.btn[i][j].config(state=tk.NORMAL, image=self.img_list[0])
                self.check[i][j] = 0
        self.gamestri = "X"


root = tk.Tk()
a = tic_tac_toe(root)
root.mainloop()
