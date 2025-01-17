import tkinter as tk
from tkinter import messagebox
import math

# Function to update the expression in the text entry box
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the contents of the text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# Function to add a decimal point
def add_decimal():
    global expression
    if '.' not in expression.split()[-1]:
        expression = expression + '.'
        equation.set(expression)

# Function to handle scientific functions
def scientific_function(func):
    global expression
    try:
        result = str(func(float(expression)))
        equation.set(result)
        expression = result
    except:
        equation.set(" error ")
        expression = ""

# Function to remove the last character from the expression
def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

# Function to handle memory add
def memory_add():
    global memory, expression
    memory += float(expression)
    expression = ""
    equation.set(expression)

# Function to handle memory subtract
def memory_subtract():
    global memory, expression
    memory -= float(expression)
    expression = ""
    equation.set(expression)

# Initialize memory
memory = 0

# Main function to create the GUI
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Scientific Calculator")
    root.geometry("600x400")  # Increased width to accommodate new buttons
    root.configure(bg='#708090')  # Dark blue background

    expression = ""
    equation = tk.StringVar()

    # Create the text entry box for showing the expression
    expression_field = tk.Entry(root, textvariable=equation, font=('times new roman', 22, 'bold'), bd=10, insertwidth=4, width=28, borderwidth=10, bg='#90ee90', fg='#000000')
    expression_field.grid(row=0, column=0, columnspan=6)

    # Create buttons and place them in the grid
    button_texts = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sin', 1, 4), ('(', 1, 5),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('cos', 2, 4), (')', 2, 5),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('tan', 3, 4), ('⌫', 3, 5),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('sqrt', 4, 4), ('^', 4, 5),
        ('Clear', 5, 0), ('log', 5, 1), ('ln', 5, 2), ('exp', 5, 3), ('π', 5, 4), ('e', 5, 5),
        ('sin⁻¹', 6, 0), ('cos⁻¹', 6, 1), ('tan⁻¹', 6, 2), ('sinh', 6, 3), ('cosh', 6, 4), ('tanh', 6, 5),
        ('sinh⁻¹', 7, 0), ('cosh⁻¹', 7, 1), ('tanh⁻¹', 7, 2), ('log₁₀', 7, 3), ('log₂', 7, 4), ('n!', 7, 5),
        ('x²', 8, 0), ('x³', 8, 1), ('xʸ', 8, 2), ('√', 8, 3), ('³√', 8, 4), ('mod', 8, 5),
        ('MC', 9, 0), ('MR', 9, 1), ('M+', 9, 2), ('M-', 9, 3), ('deg', 9, 4), ('rad', 9, 5)
    ]

    for button in button_texts:
        text, row, col = button
        action = lambda x=text: press(x) if x not in ('=', 'Clear', '.', 'sin', 'cos', 'tan', 'sqrt', 'log', 'ln', 'exp', '^', '⌫', 'π', 'e', 'sin⁻¹', 'cos⁻¹', 'tan⁻¹', 'sinh', 'cosh', 'tanh', 'sinh⁻¹', 'cosh⁻¹', 'tanh⁻¹', 'log₁₀', 'log₂', 'n!', 'x²', 'x³', 'xʸ', '√', '³√', 'mod', 'MC', 'MR', 'M+', 'M-', 'deg', 'rad') else (
            equalpress() if x == '=' else (
                clear() if x == 'Clear' else (
                    add_decimal() if x == '.' else (
                        scientific_function(getattr(math, x)) if x in ['sin', 'cos', 'tan', 'sqrt', 'log', 'ln', 'exp', 'sinh', 'cosh', 'tanh', 'log10', 'log2', 'sqrt', 'factorial'] else (
                            backspace() if x == '⌫' else (
                                press('**') if x == '^' else (
                                    press(str(math.pi)) if x == 'π' else (
                                        press(str(math.e)) if x == 'e' else (
                                            scientific_function(lambda x: math.asin(x)) if x == 'sin⁻¹' else (
                                                scientific_function(lambda x: math.acos(x)) if x == 'cos⁻¹' else (
                                                    scientific_function(lambda x: math.atan(x)) if x == 'tan⁻¹' else (
                                                        scientific_function(lambda x: math.sinh(x)) if x == 'sinh' else (
                                                            scientific_function(lambda x: math.cosh(x)) if x == 'cosh' else (
                                                                scientific_function(lambda x: math.tanh(x)) if x == 'tanh' else (
                                                                    scientific_function(lambda x: math.asinh(x)) if x == 'sinh⁻¹' else (
                                                                        scientific_function(lambda x: math.acosh(x)) if x == 'cosh⁻¹' else (
                                                                            scientific_function(lambda x: math.atanh(x)) if x == 'tanh⁻¹' else (
                                                                                scientific_function(lambda x: math.log10(x)) if x == 'log₁₀' else (
                                                                                    scientific_function(lambda x: math.log2(x)) if x == 'log₂' else (
                                                                                        scientific_function(lambda x: math.factorial(x)) if x == 'n!' else (
                                                                                            scientific_function(lambda x: x**2) if x == 'x²' else (
                                                                                                scientific_function(lambda x: x**3) if x == 'x³' else (
                                                                                                    scientific_function(lambda x: x**float(expression.split()[-1])) if x == 'xʸ' else (
                                                                                                        scientific_function(lambda x: math.sqrt(x)) if x == '√' else (
                                                                                                            scientific_function(lambda x: x**(1/3)) if x == '³√' else (
                                                                                                                scientific_function(lambda x: x % float(expression.split()[-1])) if x == 'mod' else (
                                                                                                                    clear() if x == 'MC' else (
                                                                                                                        equation.set(memory) if x == 'MR' else (
                                                                                                                            memory_add() if x == 'M+' else (
                                                                                                                                memory_subtract() if x == 'M-' else (
                                                                                                                                    press('math.degrees(') if x == 'deg' else press('math.radians(')
                                                                                                                                )
                                                                                                                            )
                                                                                                                        )
                                                                                                                    )
                                                                                                                )
                                                                                                            )
                                                                                                        )
                                                                                                    )
                                                                                                )
                                                                                            )
                                                                                        )
                                                                                    )
                                                                                )
                                                                            )
                                                                        )
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
        button = tk.Button(root, text=text, fg='#ffffff', bg='#000000', command=action, height=1, width=5, font=('Arial', 13, 'bold'))
        button.grid(row=row, column=col, padx=5, pady=5)

    root.mainloop()