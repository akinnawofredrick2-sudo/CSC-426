from tkinter import *

root = Tk()
root.title("CSC426 Calculator - Fredrick")
root.geometry("320x450")
root.resizable(False, False)

entry = Entry(root, width=25, font=("Arial", 18), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '%', '=', '+'
]

row = 1
col = 0

for btn in buttons:
    if btn == "=":
        Button(root, text=btn, width=6, height=2,
               command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        Button(root, text=btn, width=6, height=2,
               command=lambda b=btn: button_click(b)).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

Button(root, text="C", width=30, height=2,
       command=clear).grid(row=5, column=0, columnspan=4, pady=10)

root.mainloop()