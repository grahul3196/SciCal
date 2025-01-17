import streamlit as st
import math

# Function to update the expression in the text entry box
def press(num):
    global expression
    expression = expression + str(num)
    st.session_state.equation = expression

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        st.session_state.equation = total
        expression = ""
    except:
        st.session_state.equation = " error "
        expression = ""

# Function to clear the contents of the text entry box
def clear():
    global expression
    expression = ""
    st.session_state.equation = ""

# Function to add a decimal point
def add_decimal():
    global expression
    if '.' not in expression.split()[-1]:
        expression = expression + '.'
        st.session_state.equation = expression

# Function to handle scientific functions
def scientific_function(func):
    global expression
    try:
        result = str(func(float(expression)))
        st.session_state.equation = result
        expression = result
    except:
        st.session_state.equation = " error "
        expression = ""

# Function to remove the last character from the expression
def backspace():
    global expression
    expression = expression[:-1]
    st.session_state.equation = expression

# Function to handle memory add
def memory_add():
    global memory, expression
    memory += float(expression)
    expression = ""
    st.session_state.equation = expression

# Function to handle memory subtract
def memory_subtract():
    global memory, expression
    memory -= float(expression)
    expression = ""
    st.session_state.equation = expression

# Initialize memory
memory = 0

# Initialize expression
expression = ""

# Main function to create the GUI
def main():
    global expression

    st.title("Scientific Calculator")

    if 'equation' not in st.session_state:
        st.session_state.equation = ""

    st.text_input("Expression", value=st.session_state.equation, key="equation", disabled=True)

    button_texts = [
        ('7', '8', '9', '/', 'sin', '('),
        ('4', '5', '6', '*', 'cos', ')'),
        ('1', '2', '3', '-', 'tan', '⌫'),
        ('0', '.', '+', '=', 'sqrt', '^'),
        ('Clear', 'log', 'ln', 'exp', 'π', 'e'),
        ('sin⁻¹', 'cos⁻¹', 'tan⁻¹', 'sinh', 'cosh', 'tanh'),
        ('sinh⁻¹', 'cosh⁻¹', 'tanh⁻¹', 'log₁₀', 'log₂', 'n!'),
        ('x²', 'x³', 'xʸ', '√', '³√', 'mod'),
        ('MC', 'MR', 'M+', 'M-', 'deg', 'rad')
    ]

    for row in button_texts:
        cols = st.columns(len(row))
        for i, text in enumerate(row):
            with cols[i]:
                if text == '=':
                    st.button(text, on_click=equalpress)
                elif text == 'Clear':
                    st.button(text, on_click=clear)
                elif text == '.':
                    st.button(text, on_click=add_decimal)
                elif text == '⌫':
                    st.button(text, on_click=backspace)
                elif text == 'M+':
                    st.button(text, on_click=memory_add)
                elif text == 'M-':
                    st.button(text, on_click=memory_subtract)
                elif text in ['sin', 'cos', 'tan', 'sqrt', 'log', 'ln', 'exp', 'sinh', 'cosh', 'tanh', 'log₁₀', 'log₂', 'n!', 'x²', 'x³', 'xʸ', '√', '³√', 'mod']:
                    st.button(text, on_click=lambda x=text: scientific_function(getattr(math, x)))
                elif text == 'π':
                    st.button(text, on_click=lambda: press(str(math.pi)))
                elif text == 'e':
                    st.button(text, on_click=lambda: press(str(math.e)))
                elif text == 'sin⁻¹':
                    st.button(text, on_click=lambda: scientific_function(lambda x: math.asin(x)))
                elif text == 'cos⁻¹':
                    st.button(text, on_click=lambda: scientific_function(lambda x: math.acos(x)))
                elif text == 'tan⁻¹':
                    st.button(text, on_click=lambda: scientific_function(lambda x: math.atan(x)))
                elif text == 'sinh⁻¹':
                    st.button(text, on_click=lambda: scientific_function(lambda x: math.asinh(x)))
                elif text == 'cosh⁻¹':
                    st.button(text, on_click=lambda: scientific_function(lambda x: math.acosh(x)))
                elif text == 'tanh⁻¹':
                    st.button(text, on_click=lambda: scientific_function(lambda x: math.atanh(x)))
                elif text == 'xʸ':
                    st.button(text, on_click=lambda: scientific_function(lambda x: x**float(expression.split()[-1])))
                elif text == 'MC':
                    st.button(text, on_click=clear)
                elif text == 'MR':
                    st.button(text, on_click=lambda: st.session_state.equation = memory)
                elif text == 'deg':
                    st.button(text, on_click=lambda: press('math.degrees('))
                elif text == 'rad':
                    st.button(text, on_click=lambda: press('math.radians('))
                else:
                    st.button(text, on_click=lambda x=text: press(x))

if __name__ == "__main__":
    main()
