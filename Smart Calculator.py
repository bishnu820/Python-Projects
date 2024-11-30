import re  # Import regex for parsing mathematical expressions
from tkinter import *

# Basic mathematical operations
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): 
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero error"
def mod(a, b): 
    try:
        return a % b
    except ZeroDivisionError:
        return "Division by zero error"
def lcm(a, b):
    L = max(a, b)
    while L <= a * b:
        if L % a == 0 and L % b == 0:
            return L
        L += 1
def hcf(a, b):
    H = min(a, b)
    while H >= 1:
        if a % H == 0 and b % H == 0:
            return H
        H -= 1

# Extract numbers and operator from the input text
def extract_from_text(text):
    pattern = r'(-?\d+\.?\d*)\s*([+\-*/%LCMHCF]+)\s*(-?\d+\.?\d*)'
    match = re.search(pattern, text.upper())
    if match:
        num1 = float(match.group(1))
        operator = match.group(2)
        num2 = float(match.group(3))
        return num1, operator, num2
    return None, None, None

# Perform calculation
def calculate():
    text = textin.get()
    num1, operator, num2 = extract_from_text(text)
    if operator in operations:
        try:
            result = operations[operator](num1, num2)
            output_list.delete(0, END)
            output_list.insert(END, f"Result: {result}")
        except Exception as e:
            output_list.delete(0, END)
            output_list.insert(END, f"Error: {str(e)}")
    else:
        output_list.delete(0, END)
        output_list.insert(END, "Error: Unknown operation. Try again.")

# Operations dictionary
operations = {
    '+': add, 
    '-': sub, 
    '*': mul, 
    '/': div, 
    '%': mod,
    'LCM': lcm, 
    'HCF': hcf,
}

# GUI setup
win = Tk()
win.geometry('500x300')
win.title('Smart Calculator')
win.configure(bg='lightskyblue')

# Labels
Label(win, text='I am a Smart Calculator', font=('Arial', 14), bg='lightskyblue').place(x=150, y=10)
Label(win, text='My name is Human', font=('Arial', 12), bg='lightskyblue').place(x=180, y=40)
Label(win, text='What can I help you with?', font=('Arial', 12), bg='lightskyblue').place(x=165, y=130)

# Input entry
textin = StringVar()
Entry(win, width=30, textvariable=textin, font=('Arial', 12)).place(x=100, y=160)

# Button
Button(win, text='Calculate', command=calculate, font=('Arial', 12), bg='lightgreen').place(x=210, y=200)

# Output listbox
output_list = Listbox(win, width=30, height=3, font=('Arial', 12))
output_list.place(x=140, y=230)

# Start the GUI loop
win.mainloop()
