import tkinter as tk
from math import sqrt


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create display
        self.display_var = tk.StringVar()
        self.display = tk.Entry(master, textvariable=self.display_var,
                                justify='right', font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('Clear', 5, 0), ('x²', 5, 1), ('√', 5, 2), ('±', 5, 3)
        ]

        # Create buttons
        for (text, row, col) in buttons:
            btn = tk.Button(master, text=text, font=('Arial', 12),
                            command=lambda t=text: self.on_button_click(t),
                            padx=10, pady=10)
            btn.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)

        # Configure grid weights
        for i in range(6):
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

        # Initialize calculator state
        self.first_number = None
        self.operator = None
        self.new_entry = True

    def on_button_click(self, char):
        current = self.display_var.get()

        if char in '0123456789':
            if self.new_entry:
                self.display_var.set(char)
                self.new_entry = False
            else:
                self.display_var.set(current + char)

        elif char == '.':
            if '.' not in current:
                self.display_var.set(current + '.')
                self.new_entry = False

        elif char == '±':
            if current and current != '0':
                if '-' in current:
                    self.display_var.set(current[1:])
                else:
                    self.display_var.set('-' + current)

        elif char in '+-*/':
            try:
                self.first_number = float(current)
                self.operator = char
                self.new_entry = True
            except:
                self.display_var.set("Error")
                self.first_number = None
                self.operator = None

        elif char == '=':
            if self.operator and self.first_number is not None:
                try:
                    second_number = float(current)
                    if self.operator == '+':
                        result = self.first_number + second_number
                    elif self.operator == '-':
                        result = self.first_number - second_number
                    elif self.operator == '*':
                        result = self.first_number * second_number
                    elif self.operator == '/':
                        result = self.first_number / second_number
                    self.display_var.set(result)
                    self.operator = None
                    self.first_number = None
                    self.new_entry = True
                except Exception as e:
                    self.display_var.set("Error")
                    self.operator = None
                    self.first_number = None

        elif char == 'Clear':
            self.display_var.set('')
            self.first_number = None
            self.operator = None
            self.new_entry = True

        elif char == 'x²':
            try:
                num = float(current)
                self.display_var.set(num ** 2)
                self.new_entry = True
            except:
                self.display_var.set("Error")

        elif char == '√':
            try:
                num = float(current)
                if num < 0:
                    raise ValueError
                self.display_var.set(sqrt(num))
                self.new_entry = True
            except:
                self.display_var.set("Error")


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()