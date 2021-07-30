from tkinter import *
import math
from idlelib.tooltip import Hovertip
from decimal import Decimal
import os
import sys
#Functionality
Num1 = ""
Num2 = ""
OpCar = ""
First = True
res = ""
sign = "positive"
Acum = ""
#Numbers, First or Second
def GetNumber(Num):
    global First
    global Acum
    if First == True:
        global Num1
        Num1 = Num1 + str(Num)
        Acum = Num1
        screen_calc.configure(text=str(Num1))
        screenA_calc.configure(text=str(Acum))
    else:
        global Num2
        Num2 = Num2 + str(Num)
        Acum = Acum + " " + str(Num2)
        screen_calc.configure(text=str(Num2))
        screenA_calc.configure(text=str(Acum))
#Operation Characters
def GetOpNormal(OpfbuttonN):
    global OpCar
    if OpCar == "":
        global Acum
        global First
        OpCar = str(OpfbuttonN)
        First = False
        Acum = Acum + " " + str(OpCar)
        screenA_calc.configure(text=Acum)
        screen_calc.configure(text="")
    else:
        print("ERROR")
def GetOpDiferent(OpfbuttonF):
    global OpCar
    global Acum
    if OpCar == "":
        global First
        OpCar = str(OpfbuttonF)
        First = True
        Acum = Acum + " " + str(OpCar)
        screen_calc.configure(text="")
        screenA_calc.configure(text=Acum)
    else:
        print("ERROR")
def GetDel():
    global Num1
    global Num2
    global Acum
    if First == True:
        Num1 = Num1[:-1]
        Acum = Acum[:-1]
        screen_calc.configure(text=Num1)
        screenA_calc.configure(text=Acum)
    else:
        Num2 = Num2[:-1]
        Acum = Acum[:-1]
        screen_calc.configure(text=Num2)
        screenA_calc.configure(text=Acum)
def GetCE():
    global OpCar
    global First
    global Num1
    global Num2
    global Acum
    Acum = ""
    OpCar = ""
    Num1 = ""
    Num2 = ""
    First = True
    screen_calc.configure(text="")
    screenA_calc.configure(text="")
def GetDot():
    global First
    global Num1
    global Num2
    global Acum
    if First == True:
        Num1 = Num1 + "."
        Acum = Acum + "."
        screen_calc.configure(text=Num1)
        screenA_calc.configure(text=Acum)
    else:
        Num2 = Num2 + "."
        screen_calc.configure(text=Num2)
def GetSign():
    global sign
    global Num1
    global Num2
    if sign == "positive":
        sign = "negative"
        if First == True:
            Num1 = "-" + Num1
            screen_calc.configure(text=Num1)
        else:
            Num2 = "-" + Num2
            screen_calc.configure(text=Num2)
    else:
        sign = "positive"
        if First == True:
            Num1 = Num1.lstrip("-")
            screen_calc.configure(text=Num1)
        else:
            Num2 = Num2.lstrip("-")
            screen_calc.configure(text=Num2)
#Equal Function
def Equal():
    global OpCar
    global res
    global Num1
    global Num2
    global First
    global Acum
    Acum = ""
    if OpCar == "+":
        res = float(Num1)+float(Num2)
        print(res)
    elif OpCar == "-":
        res = float(Decimal(Num1)-Decimal(Num2))
        print(res)
    elif OpCar == "/":
        try:
            res = float(Num1)/float(Num2)
            print(res)
        except ZeroDivisionError:
            res = "Math_Error"
            print(res)
    elif OpCar == "x":
        res = float(Num1)*float(Num2)
        print(res)
    elif OpCar == "^":
        res = float(Num1)*float(Num1)
        print(res)
    elif OpCar == "root":
        res = math.sqrt(float(Num1))
        print(res)
    else:
        pass
    screen_calc.configure(text=str(res))
    OpCar = ""
    Num1 = res
    Acum = "Ans"
    screenA_calc.configure(text=str(Acum))
    Num2 = ""
    res = ""
    First = False
def OpenSettings():
    GetCE()
    calc_win.destroy
    settings_win = Tk()
    settings_win.geometry("200x360")
    settings_win.resizable(True, True)
    settings_win.title("Settings")
    settings_win.iconbitmap((os.path.join(sys.path[0], "windowIcon.ico")))
    settings_win.configure(bg="gray20")
    settings_win.mainloop()
#################################################################################
#GUI
#Window config
calc_win = Tk()
calc_win.geometry("300x460")
calc_win.resizable(True, True)
calc_win.title("Simple GUI Calculator")
calc_win.iconbitmap((os.path.join(sys.path[0], "windowIcon.ico")))
calc_win.configure(bg="gray20")
#Settings button
buttonSettings= Button(calc_win, text="Settings", width=18, height=1, command=OpenSettings)
buttonSettings.grid(row=0, column = 0, columnspan=2)
#Screen Acumulative label (Row 0)
screenA_calc = Label(calc_win, text="", width=21, height=1, bg="white", anchor="w")
screenA_calc.grid(row=0, columnspan=2, column=2, pady=(5))
#Screen label (Row 1)
screen_calc = Label(calc_win, text="", width=42, height=3, bg="white", anchor="w")
screen_calc.grid(row=1, columnspan=4, pady=(15))
#Clear and delete button (Row 2)
buttonClear= Button(calc_win, text="CE", width=18, height=2, command=GetCE)
buttonClear.grid(row=2, column = 0, columnspan=2)
buttonDelete= Button(calc_win, text="DEL", width=18, height=2, command=GetDel)
buttonDelete.grid(row=2, column = 2, columnspan=2)
#Square, square root and division (Row 3)
buttonSquare= Button(calc_win, text="X^2", width=9, height=2, command=lambda:GetOpDiferent("^"))
buttonSquare.grid(row=3, column = 0, pady=(10))
buttonRoot= Button(calc_win, text="√X", width=9, height=2, command=lambda:GetOpDiferent("root"))
buttonRoot.grid(row=3, column = 1)
buttonDiv= Button(calc_win, text="/", width=18, height=2, command=lambda:GetOpNormal("/"))
buttonDiv.grid(row=3, column = 2, columnspan=2)
#7, 8, 9 and multiplication (Row 4)
button7= Button(calc_win, text="7", width=9, height=2, command=lambda:GetNumber("7"))
button7.grid(row=4,column=0, pady=(10))
button8= Button(calc_win, text="8", width=9, height=2, command=lambda:GetNumber("8"))
button8.grid(row=4,column=1)
button9= Button(calc_win, text="9", width=9, height=2, command=lambda:GetNumber("9"))
button9.grid(row=4,column=2)
buttonMult= Button(calc_win, text="X", width=9, height=2, command=lambda:GetOpNormal("x"))
buttonMult.grid(row=4,column=3)
#4, 5, 6 and Subtraction (Row 5)
button4= Button(calc_win, text="4", width=9, height=2, command=lambda:GetNumber("4"))
button4.grid(row=5,column=0, pady=(10))
button5= Button(calc_win, text="5", width=9, height=2, command=lambda:GetNumber("5"))
button5.grid(row=5,column=1)
button6= Button(calc_win, text="6", width=9, height=2, command=lambda:GetNumber("6"))
button6.grid(row=5,column=2)
buttonSub= Button(calc_win, text="-", width=9, height=2, command=lambda:GetOpNormal("-"))
buttonSub.grid(row=5,column=3)
#1, 2, 3 and Add (Row 6)
button1= Button(calc_win, text="1", width=9, height=2, command=lambda:GetNumber("1"))
button1.grid(row=6,column=0, pady=(10))
button2= Button(calc_win, text="2", width=9, height=2, command=lambda:GetNumber("2"))
button2.grid(row=6,column=1)
button3= Button(calc_win, text="3", width=9, height=2, command=lambda:GetNumber("3"))
button3.grid(row=6,column=2)
buttonAdd= Button(calc_win, text="+", width=9, height=2, command=lambda:GetOpNormal("+"))
buttonAdd.grid(row=6,column=3)
#+/-, 0, . and Equal (Row 7)
buttonPlusorminus= Button(calc_win, text="+/-", width=9, height=2, command=GetSign)
buttonPlusorminus.grid(row=7,column=0, pady=(10))
button0= Button(calc_win, text="0", width=9, height=2, command=lambda:GetNumber("0"))
button0.grid(row=7,column=1)
buttonDot= Button(calc_win, text=".", width=9, height=2, command=GetDot)
buttonDot.grid(row=7,column=2)
buttonEqual= Button(calc_win, text="=", width=9, height=2, command=Equal)
buttonEqual.grid(row=7,column=3)
##########################################
#Key Bindings
calc_win.bind('1', lambda event: GetNumber("1"))
Hovertip(button1, '1')
calc_win.bind('2', lambda event: GetNumber("2"))
Hovertip(button2, '2')
calc_win.bind('3', lambda event: GetNumber("3"))
Hovertip(button3, '3')
calc_win.bind('4', lambda event: GetNumber("4"))
Hovertip(button4, '4')
calc_win.bind('5', lambda event: GetNumber("5"))
Hovertip(button5, '5')
calc_win.bind('6', lambda event: GetNumber("6"))
Hovertip(button6, '6')
calc_win.bind('7', lambda event: GetNumber("7"))
Hovertip(button7, '7')
calc_win.bind('8', lambda event: GetNumber("8"))
Hovertip(button8, '8')
calc_win.bind('9', lambda event: GetNumber("9"))
Hovertip(button9, '9')
calc_win.bind('0', lambda event: GetNumber("0"))
Hovertip(button0, '0')
calc_win.bind('+', lambda event: GetOpNormal("+"))
Hovertip(buttonAdd, '+')
calc_win.bind('-', lambda event: GetOpNormal("-"))
Hovertip(buttonSub, '-')
calc_win.bind('*', lambda event: GetOpNormal("x"))
Hovertip(buttonMult, '*')
calc_win.bind('/', lambda event: GetOpNormal("/"))
Hovertip(buttonDiv, '/')
calc_win.bind('.', lambda event: GetDot())
Hovertip(buttonDot, '.')
calc_win.bind('<Return>', lambda event: Equal())
Hovertip(buttonEqual, 'Enter')
calc_win.bind('<Alt-s>', lambda event: GetSign())
Hovertip(buttonPlusorminus, 'Alt+s')
calc_win.bind('<Alt-c>', lambda event: GetCE())
Hovertip(buttonClear, 'Alt+c')
calc_win.bind('<Alt-r>', lambda event: GetOpDiferent("root"))
Hovertip(buttonRoot, 'Alt+r')
calc_win.bind('<Alt-q>', lambda event: GetOpDiferent("^"))
Hovertip(buttonSquare, 'Alt+q')
calc_win.bind('<BackSpace>', lambda event: GetDel())
Hovertip(buttonDelete, 'Delete')
calc_win.mainloop()
