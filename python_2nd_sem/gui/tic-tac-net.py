import tkinter as tk

class TicTacToeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.label1 = tk.Label(master, text="Tic-Tac-Toe Game", font=("comicsansms", 15, "bold"))
        self.label1.grid(row=0, column=0, columnspan=3)

        self.gamestr = "X"
        self.buttons = [[None, None, None] for _ in range(3)]
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(master, text="", command=lambda row=i, col=j: self.write_it(row, col))
                self.buttons[i][j].grid(row=i+1, column=j, ipadx=40, ipady=40)

    def write_it(self, row, col):
        if self.buttons[row][col]['text'] == "":
            self.buttons[row][col].config(text=self.gamestr)
            if self.gamestr == "X":
                self.gamestr = "O"
            else:
                self.gamestr = "X"
            self.checker()

    def checker(self):
    # Check rows
        for row in self.buttons:
            if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
                print(f"{row[0]['text']} wins!")
                return
    
        # Check columns
        for col in range(3):
            if self.buttons[0][col]['text'] == self.buttons[1][col]['text'] == self.buttons[2][col]['text'] != "":
                print(f"{self.buttons[0][col]['text']} wins!")
                return
    
        # Check diagonals
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            print(f"{self.buttons[0][0]['text']} wins!")
            return
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            print(f"{self.buttons[0][2]['text']} wins!")
            return
    
        # Check for a draw
        if all(button['text'] != "" for row in self.buttons for button in row):
            print("The game is a draw!")
            return
    
            
    
            

        

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
