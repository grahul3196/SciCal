import streamlit as st
import math

# Function to update the expression in the text entry box
def press(num):
    st.session_state.expression += str(num)
    st.session_state.equation = st.session_state.expression

# Function to evaluate the final expression
def equalpress():
    try:
        st.session_state.equation = str(eval(st.session_state.expression))
        st.session_state.expression = ""
    except:
        st.session_state.equation = " error "
        st.session_state.expression = ""

# Function to clear the contents of the text entry box
def clear():
    st.session_state.expression = ""
    st.session_state.equation = ""

# Initialize session state variables
if 'expression' not in st.session_state:
    st.session_state.expression = ""
if 'equation' not in st.session_state:
    st.session_state.equation = ""

# Main function to create the GUI
def main():
    st.title("Scientific Calculator")

    st.text_input("Expression", value=st.session_state.equation, key="equation", disabled=True)

    button_texts = [
        ('7', '8', '9', '/'),
        ('4', '5', '6', '*'),
        ('1', '2', '3', '-'),
        ('0', '.', '+', '='),
        ('Clear',)
    ]

    for row in button_texts:
        cols = st.columns(len(row))
        for i, text in enumerate(row):
            with cols[i]:
                if text == '=':
                    st.button(text, on_click=equalpress)
                elif text == 'Clear':
                    st.button(text, on_click=clear)
                else:
                    st.button(text, on_click=lambda x=text: press(x))

if __name__ == "__main__":
    main()


