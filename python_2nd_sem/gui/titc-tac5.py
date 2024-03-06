import tkinter as tk
from tkinter import simpledialog, messagebox

class TicTacToeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.label1 = tk.Label(master, text="Tic-Tac-Toe Game", font=("comicsansms", 15, "bold"))
        self.label1.grid(row=0, column=0, columnspan=3)

        self.player_x = self.get_player_name("X")
        self.player_o = self.get_player_name("O")
        self.current_player = "X"

        self.buttons = [[None, None, None] for _ in range(3)]

        self.frame_winner = tk.Frame(master)
        self.label_winner = tk.Label(self.frame_winner, text="", font=("comicsansms", 12, "bold"))
        self.label_winner.pack()
        self.frame_winner.grid(row=5, column=0, columnspan=3)

        for i in range(3):
            for j in range(3):
                button = tk.Button(master, text="", command=lambda row=i, col=j: self.write_it(row, col),
                                   font=("comicsansms", 15, "bold"))
                button.grid(row=i + 1, column=j, ipadx=40, ipady=40)
                button.config(bg="green")
                self.buttons[i][j] = button

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=4, column=1)

    def get_player_name(self, symbol):
        return simpledialog.askstring(f"Player {symbol}", f"Enter name for Player {symbol}")

    def write_it(self, row, col):
        button = self.buttons[row][col]
        if button['text'] == "":
            button.config(text=self.current_player, state=tk.DISABLED, bg="red")
            self.master.after(1000, lambda: button.config(bg="green", state=tk.NORMAL))
            if self.check_winner():
                self.show_winner()
            elif self.check_draw():
                self.show_draw()
            else:
                self.toggle_player()

    def toggle_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if (self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != "" or
                    self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != ""):
                return True
        if (self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "" or
                self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != ""):
            return True
        return False

    def show_winner(self):
        winner = self.current_player
        winner_name = self.player_x if winner == "X" else self.player_o
        self.label_winner.config(text=f"{winner_name} ({winner}) wins!")

    def check_draw(self):
        return all(button['text'] != "" for row in self.buttons for button in row)

    def show_draw(self):
        self.label_winner.config(text="The game is a draw!")

    def reset_game(self):
        for row in self.buttons:
            for button in row:
                button.config(text="", state=tk.NORMAL, bg="green")
        self.label_winner.config(text="")
        self.current_player = "X"


root = tk.Tk()
app = TicTacToeApp(root)
root.mainloop()
