import tkinter as tk

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("tic tac toe")

        self.label1 = tk.Label(master, text="Tic-Tac-Toe Game ",font=("comicsansms", 15, "bold"))
        self.label1.grid(row=0,column=2)

        self.gamestr = "X"
        
        #row1

        self.add_button1 = tk.Button(master, text="", command=lambda: self.write_it(self.add_button1))
        self.add_button1.grid(row=1, column=1, ipadx=40, ipady=40)
        
        self.add_button2 = tk.Button(master, text="", command=lambda: self.write_it(self.add_button2))
        self.add_button2.grid(row=1, column=2, ipadx=40, ipady=40)
        
        self.add_button3 = tk.Button(master, text="", command=lambda: self.write_it(self.add_button3))
        self.add_button3.grid(row=1, column=3, ipadx=40, ipady=40)
        
        #row2
    
        self.add_button4 = tk.Button(master, text="", command=lambda: self.write_it(self.add_button4))
        self.add_button4.grid(row=2, column=1, ipadx=40, ipady=40)
        
        self.add_button5 = tk.Button(master, text="", command=lambda: self.write_it(self.add_button5))
        self.add_button5.grid(row=2, column=2, ipadx=40, ipady=40)
        
        self.add_button6 = tk.Button(master, text="", command=lambda: self.write_it(self.add_button6))
        self.add_button6.grid(row=2, column=3, ipadx=40, ipady=40)
        
        #row3
        
        self.add_button7 = tk.Button(master, text="", command=lambda: self.write_it(self.add_button7))
        self.add_button7.grid(row=3, column=1, ipadx=40, ipady=40)
        
        self.add_button8 = tk.Button(master, text="", command=lambda: self.write_it(self.add_button8))
        self.add_button8.grid(row=3, column=2, ipadx=40, ipady=40)
        
        self.add_button9 = tk.Button(master, text="", command=lambda: self.write_it(self.add_button9))
        self.add_button9.grid(row=3, column=3, ipadx=40, ipady=40)

    def write_it(self, btn):
        if btn['text'] == "":
            btn.config(text=self.gamestr)
            if self.gamestr == "X":
                self.gamestr = "O"
            else:
                self.gamestr = "X"
        self.checker()

    def checker(self):
        
        #row
        for row in self.add_button1,self.add_button2,self.add_button3:
            if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
                print(f"{row[0]['text']} wins!")
                
        for row in self.add_button4,self.add_button5,self.add_button6:
            if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
                print(f"{row[0]['text']} wins!")
        for row in self.add_button7,self.add_button8,self.add_button6:
            if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
                print(f"{row[0]['text']} wins!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

































# def checker(self):
#     # Check rows
#     for i in range(3):
#         if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != "":
#             print(f"{self.buttons[i][0]['text']} wins!")
#             return

#     # Check columns
#     for i in range(3):
#         if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != "":
#             print(f"{self.buttons[0][i]['text']} wins!")
#             return

#     # Check diagonals
#     if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
#         print(f"{self.buttons[0][0]['text']} wins!")
#         return
#     if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
#         print(f"{self.buttons[0][2]['text']} wins!")
#         return

#     # Check if the game is a draw
#     if all(self.buttons[i][j]['text'] != "" for i in range(3) for j in range(3)):
#         print("The game is a draw!")
#         return
