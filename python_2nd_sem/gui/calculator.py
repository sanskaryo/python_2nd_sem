import tkinter as tk
import ast

class Calculator:
    def __init__(self, root):
        self.expression = ""
        self.equation = tk.StringVar()

        # Create the text entry box for showing the expression
        self.expression_field = tk.Entry(root, textvariable=self.equation)
        self.expression_field.grid(columnspan=4, ipadx=65)

        # Define digit buttons
        for i in range(1, 10):
            row_val = (i - 1) // 3 + 2
            col_val = (i - 1) % 3
            btn = tk.Button(root, text=str(i), fg='black', bg='white', command=lambda i=i: self.Press(i), height=1, width=7)
            btn.grid(row=row_val, column=col_val)

        # Define 0 button
        button0 = tk.Button(root, text='0', fg='black', bg='white', command=lambda: self.Press(0), height=1, width=7)
        button0.grid(row=5, column=1)

        # Define operator buttons
        operators = ['+', '-', '*', '/']
        for i, operator in enumerate(operators):
            btn = tk.Button(root, text=operator, fg='black', bg='white', command=lambda operator=operator: self.Press(operator), height=1, width=7)
            btn.grid(row=i + 2, column=3)

        # Define equal button
        equal_button = tk.Button(root, text='=', fg='black', bg='white', command=self.equalPress, height=1, width=7)
        equal_button.grid(row=5, column=2)

        # Define clear button
        clear_button = tk.Button(root, text='C', fg='black', bg='white', command=self.clear, height=1, width=7)
        clear_button.grid(row=5, column=0)

    def Press(self, value):
        self.expression += str(value)
        self.equation.set(self.expression)

    def equalPress(self):
        try:
            # Validate the expression using a whitelist instead of eval
            valid_chars = "0123456789+-*/."
            for char in self.expression:
                if char not in valid_chars:
                    raise ValueError("Invalid character in expression")

            # Convert valid expression to a mathematical expression using ast.literal_eval
            total = str(ast.literal_eval(self.expression))

            self.equation.set(total)
            self.expression = ""

        except (ValueError, SyntaxError):
            self.equation.set("error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.equation.set("")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("300x250")
    root.resizable(False, False)
    root.config(background="violet")

    calculator = Calculator(root)

    root.mainloop()
