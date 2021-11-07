from tkinter import *

root = Tk()
# root.geometry("250x300")
root.title("Calculator")
input = Entry(root, width=37, borderwidth=5)
input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# functions
def button_click(number):
    current = str(input.get())
    input.delete(0, END)
    input.insert(0, current + str(number))


# clear
def clear():
    current = str(input.get())
    input.delete(len(current) - 1)


def addition():
    global f_number
    f_number = int(input.get())
    global math
    math = 'addition'
    input.delete(0, END)


def equals():
    second_number = int(input.get())
    input.delete(0, END)
    if math == 'addition':
        input.insert(0, f_number + second_number)
    elif math == 'subtraction':
        input.insert(0, f_number - second_number)
    elif math == 'multiplication':
        input.insert(0, f_number * second_number)
    elif math == 'division':
        input.insert(0, f_number / second_number)


def subtraction():
    global f_number
    f_number = int(input.get())
    global math
    math = 'subtraction'
    input.delete(0, END)


def multiplication():
    global f_number
    f_number = int(input.get())
    global math
    math = 'multiplication'
    input.delete(0, END)


def division():
    global f_number
    f_number = int(input.get())
    global math
    math = 'division'
    input.delete(0, END)


# buttons
button_1 = Button(root, text="1", padx=40, pady=20, bg="black", fg="white", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, bg="black", fg="white", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=48, pady=20, bg="black", fg="white", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, bg="black", fg="white", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, bg="black", fg="white", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=48, pady=20, bg="black", fg="white", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, bg="black", fg="white", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, bg="black", fg="white", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=48, pady=20, bg="black", fg="white", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, bg="black", fg="white", command=lambda: button_click(0))
button_Plus = Button(root, text="+", padx=39, pady=20, bg="black", fg="red", command=addition)
button_Subtract = Button(root, text="-", padx=40, pady=20, bg="black", fg="red", command=subtraction)
button_Divide = Button(root, text="/", padx=49, pady=20, bg="black", fg="red", command=division)
button_Multiply = Button(root, text="x", padx=40, pady=20, bg="black", fg="red", command=multiplication)
button_equals = Button(root, text="=", padx=93, pady=20, bg="black", fg="red", command=equals)
button_clear = Button(root, text="Clear", padx=84, pady=20, bg="black", fg="red", command=clear)
# putting on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_Plus.grid(row=5, column=0)
button_Multiply.grid(row=6, column=0)
button_Subtract.grid(row=6, column=1)
button_Divide.grid(row=6, column=2)
button_equals.grid(row=5, column=1, columnspan=2)
root.mainloop()
