from tkinter import *
from tkinter.tix import *
from math import *
from decimal import *
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
        res = sqrt(float(Num1))
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
#################################################################################
#GUI
#Window config
calc_win = Tk()
calc_win.geometry("300x460")
calc_win.resizable(False, False)
calc_win.title("Simple GUI Calculator")
calc_win.iconbitmap("./windowIcon.ico")
calc_win.configure(bg="gray20")
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
tip = Balloon(calc_win)
calc_win.bind('1', lambda event: GetNumber("1"))
tip.bind_widget(button1 ,balloonmsg="1")
calc_win.bind('2', lambda event: GetNumber("2"))
tip.bind_widget(button2 ,balloonmsg="2")
calc_win.bind('3', lambda event: GetNumber("3"))
tip.bind_widget(button3 ,balloonmsg="3")
calc_win.bind('4', lambda event: GetNumber("4"))
tip.bind_widget(button4 ,balloonmsg="4")
calc_win.bind('5', lambda event: GetNumber("5"))
tip.bind_widget(button5 ,balloonmsg="5")
calc_win.bind('6', lambda event: GetNumber("6"))
tip.bind_widget(button6 ,balloonmsg="6")
calc_win.bind('7', lambda event: GetNumber("7"))
tip.bind_widget(button7 ,balloonmsg="7")
calc_win.bind('8', lambda event: GetNumber("8"))
tip.bind_widget(button8 ,balloonmsg="8")
calc_win.bind('9', lambda event: GetNumber("9"))
tip.bind_widget(button9 ,balloonmsg="9")
calc_win.bind('0', lambda event: GetNumber("0"))
tip.bind_widget(button0 ,balloonmsg="0")
calc_win.bind('+', lambda event: GetOpNormal("+"))
tip.bind_widget(buttonAdd ,balloonmsg="+")
calc_win.bind('-', lambda event: GetOpNormal("-"))
tip.bind_widget(buttonSub ,balloonmsg="-")
calc_win.bind('*', lambda event: GetOpNormal("x"))
tip.bind_widget(buttonMult ,balloonmsg="*")
calc_win.bind('/', lambda event: GetOpNormal("/"))
tip.bind_widget(buttonDiv ,balloonmsg="/")
calc_win.bind('.', lambda event: GetDot())
tip.bind_widget(buttonDot ,balloonmsg=".")
calc_win.bind('<Return>', lambda event: Equal())
tip.bind_widget(buttonEqual ,balloonmsg="Enter")
calc_win.bind('<Alt-s>', lambda event: GetSign())
tip.bind_widget(buttonPlusorminus ,balloonmsg="Alt+s")
calc_win.bind('<Alt-c>', lambda event: GetCE())
tip.bind_widget(buttonClear ,balloonmsg="Alt+c")
calc_win.bind('<Alt-r>', lambda event: GetOpDiferent("root"))
tip.bind_widget(buttonRoot ,balloonmsg="Alt+r")
calc_win.bind('<Alt-q>', lambda event: GetOpDiferent("^"))
tip.bind_widget(buttonSquare ,balloonmsg="Alt+q")
calc_win.bind('<BackSpace>', lambda event: GetDel())
tip.bind_widget(buttonDelete ,balloonmsg="Delete")
calc_win.mainloop()