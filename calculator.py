import tkinter
from tkinter import *

window = tkinter.Tk()
# window.geometry('312x324')
window.title('Calculator')
window.resizable(0, 0)

screen = tkinter.Label(window, text='', width=44, height=3)
screen.grid(row=0, column=0, columnspan=5)

def buttonclick(val):
    screen.config(text=screen.cget('text')+val)

def clr():
    screen.config(text='')

def equal():
    try:
        display_val = screen.cget('text')
        screen.config(text=eval(display_val))
    except:
        screen.config(text='SYNTAX ERROR')

class button_id():
    def __init__(self, value, width, height):
        self.value = value
        self.width = width
        self.height = height

c_button = button_id('C', 234, 54)
tkinter.Button(window, text=c_button.value, width=33, height=3, command=lambda: clr()).grid(row=1, column=0, columnspan=3)

divide_button = button_id('/', 78, 54)
tkinter.Button(window, text=divide_button.value, width=11, height=3, command=lambda: buttonclick('/')).grid(row=1, column=3, columnspan=1)

multiply_button = button_id('*', 78, 54)
tkinter.Button(window, text=multiply_button.value, width=11, height=3, command=lambda: buttonclick('*')).grid(row=2, column=3, columnspan=1)

subtract_button = button_id('-', 78, 54)
tkinter.Button(window, text=subtract_button.value, width=11, height=3, command=lambda: buttonclick('-')).grid(row=3, column=3, columnspan=1)

add_button = button_id('+', 78, 54)
tkinter.Button(window, text=add_button.value, width=11, height=3, command=lambda: buttonclick('+')).grid(row=4, column=3, columnspan=1)

equals_button = button_id('=', 78, 54)
tkinter.Button(window, text=equals_button.value, width=11, height=3, command=lambda: equal()).grid(row=5, column=3, columnspan=1)

point_button = button_id('.', 78, 54)
tkinter.Button(window, text=point_button.value, width=11, height=3, command=lambda: buttonclick('.')).grid(row=5, column=2, columnspan=1)

zero_button = button_id('0', 156, 54)
tkinter.Button(window, text=zero_button.value, width=22, height=3, command=lambda: buttonclick('0')).grid(row=5, column=0, columnspan=2)

one_button = button_id('1', 78, 54)
tkinter.Button(window, text=one_button.value, width=11, height=3, command=lambda: buttonclick('1')).grid(row=4, column=0, columnspan=1)

two_button = button_id('2', 78, 54)
tkinter.Button(window, text=two_button.value, width=11, height=3, command=lambda: buttonclick('2')).grid(row=4, column=1, columnspan=1)

three_button = button_id('3', 78, 54)
tkinter.Button(window, text=three_button.value, width=11, height=3, command=lambda: buttonclick('3')).grid(row=4, column=2, columnspan=1)

four_button = button_id('4', 78, 54)
tkinter.Button(window, text=four_button.value, width=11, height=3, command=lambda: buttonclick('4')).grid(row=3, column=0, columnspan=1)

five_button = button_id('5', 78, 54)
tkinter.Button(window, text=five_button.value, width=11, height=3, command=lambda: buttonclick('5')).grid(row=3, column=1, columnspan=1)

six_button = button_id('6', 78, 54)
tkinter.Button(window, text=six_button.value, width=11, height=3, command=lambda: buttonclick('6')).grid(row=3, column=2, columnspan=1)

seven_button = button_id('7', 78, 54)
tkinter.Button(window, text=seven_button.value, width=11, height=3, command=lambda: buttonclick('7')).grid(row=2, column=0, columnspan=1)

eight_button = button_id('8', 78, 54)
tkinter.Button(window, text=eight_button.value, width=11, height=3, command=lambda: buttonclick('8')).grid(row=2, column=1, columnspan=1)

nine_button = button_id('9', 78, 54)
tkinter.Button(window, text=nine_button.value, width=11, height=3, command=lambda: buttonclick('9')).grid(row=2, column=2, columnspan=1)

window.mainloop()