# import tkinter

# root = tkinter.Tk()
# root.title("my first gui program with py and tkinter")
# root.minsize(width=500, height=300)

# my_label = tkinter.Label(text="Hello Duniya", font=("Arial", 24, "italic"))
# my_label.pack(side="left")


# root.mainloop()

class Flatten:
    def __init__(self, lst):
        self.lst = lst

    def flatten(self):
        flat_list = self._flatten_recursive(self.lst)
        print(flat_list)

    def _flatten_recursive(self, nested_lst):
        result = []
        for i in nested_lst:
            if isinstance(i, list):
                result.extend(self._flatten_recursive(i))
            else:
                result.append(i)
        return result


# Example Usage:
nested_list = [1, [2, [3, 4]], 5, [6, 7, [8, 9]]]
flattener = Flatten(nested_list)
flattener.flatten()

