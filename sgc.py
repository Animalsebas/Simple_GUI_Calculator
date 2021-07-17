from tkinter import *
from math import sqrt
#Functionality
Num1 = ""
Num2 = ""
OpCar = ""
First = True
res = ""
sign = "positive"
#Numbers, First or Second
def GetNumber(Num):
    global First
    if First == True:
        global Num1
        Num1 = Num1 + str(Num)
        screen_calc.configure(text=str(Num1))
    else:
        global Num2
        Num2 = Num2 + str(Num)
        screen_calc.configure(text=str(Num2))
#Operation Characters
def GetOpNormal(OpfbuttonN):
    global OpCar
    if OpCar == "":
        global First
        OpCar = str(OpfbuttonN)
        First = False
        screen_calc.configure(text="")
    else:
        print("ERROR")
def GetOpDiferent(OpfbuttonF):
    global OpCar
    if OpCar == "":
        global First
        OpCar = str(OpfbuttonF)
        First = True
        screen_calc.configure(text="")
    else:
        print("ERROR")
def GetDel():
    global Num1
    global Num2
    if First == True:
        Num1 = Num1[:-1]
        screen_calc.configure(text=Num1)
    else:
        Num2 = Num2[:-1]
        screen_calc.configure(text=Num2)
def GetCE():
    global OpCar
    global First
    global Num1
    global Num2
    OpCar = ""
    Num1 = ""
    Num2 = ""
    First = True
    screen_calc.configure(text="")
def GetDot():
    global First
    global Num1
    global Num2
    if First == True:
        Num1 = Num1 + "."
        screen_calc.configure(text=Num1)
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
    if OpCar == "+":
        res = float(Num1)+float(Num2)
        print(res)
    elif OpCar == "-":
        res = float(Num1)-float(Num2)
        print(res)
    elif OpCar == "/":
        try:
            res = float(Num1)/float(Num2)
            print(res)
        except ZeroDivisionError:
            res = "Math_Error"
            print(res)
    elif OpCar == "X":
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
    Num1 = ""
    Num2 = ""
    res = ""
    First = True
#################################################################################
#GUI
#Window config
calc_win = Tk()
calc_win.geometry("300x450")
calc_win.resizable(False, False)
calc_win.title("Simple GUI Calculator")
calc_win.iconbitmap("./windowIcon.ico")
calc_win.configure(bg="gray20")
#Screen label (Row 0)
screen_calc = Label(calc_win, text="", width=42, height=3, bg="white", anchor="w")
screen_calc.grid(row=0, columnspan=4, pady=(15))
#Clear and delete button (Row 1)
buttonClear= Button(calc_win, text="CE", width=18, height=2, command=GetCE)
buttonClear.grid(row=1, column = 0, columnspan=2)
buttonDelete= Button(calc_win, text="DEL", width=18, height=2, command=GetDel)
buttonDelete.grid(row=1, column = 2, columnspan=2)
#Square, square root and division (Row 2)
buttonSquare= Button(calc_win, text="X^2", width=9, height=2, command=lambda:GetOpDiferent("^"))
buttonSquare.grid(row=2, column = 0, pady=(10))
buttonRoot= Button(calc_win, text="√X", width=9, height=2, command=lambda:GetOpDiferent("root"))
buttonRoot.grid(row=2, column = 1)
buttonDiv= Button(calc_win, text="/", width=18, height=2, command=lambda:GetOpNormal("/"))
buttonDiv.grid(row=2, column = 2, columnspan=2)
#7, 8, 9 and multiplication (Row 3)
button7= Button(calc_win, text="7", width=9, height=2, command=lambda:GetNumber("7"))
button7.grid(row=3,column=0, pady=(10))
button8= Button(calc_win, text="8", width=9, height=2, command=lambda:GetNumber("8"))
button8.grid(row=3,column=1)
button9= Button(calc_win, text="9", width=9, height=2, command=lambda:GetNumber("9"))
button9.grid(row=3,column=2)
buttonMult= Button(calc_win, text="X", width=9, height=2, command=lambda:GetOpNormal("X"))
buttonMult.grid(row=3,column=3)
#4, 5, 6 and Subtraction (Row 4)
button4= Button(calc_win, text="4", width=9, height=2, command=lambda:GetNumber("4"))
button4.grid(row=4,column=0, pady=(10))
button5= Button(calc_win, text="5", width=9, height=2, command=lambda:GetNumber("5"))
button5.grid(row=4,column=1)
button6= Button(calc_win, text="6", width=9, height=2, command=lambda:GetNumber("6"))
button6.grid(row=4,column=2)
buttonSub= Button(calc_win, text="-", width=9, height=2, command=lambda:GetOpNormal("-"))
buttonSub.grid(row=4,column=3)
#1, 2, 3 and Add (Row 5)
button1= Button(calc_win, text="1", width=9, height=2, command=lambda:GetNumber("1"))
button1.grid(row=5,column=0, pady=(10))
button2= Button(calc_win, text="2", width=9, height=2, command=lambda:GetNumber("2"))
button2.grid(row=5,column=1)
button3= Button(calc_win, text="3", width=9, height=2, command=lambda:GetNumber("3"))
button3.grid(row=5,column=2)
buttonAdd= Button(calc_win, text="+", width=9, height=2, command=lambda:GetOpNormal("+"))
buttonAdd.grid(row=5,column=3)
#+/-, 0, . and Equal (Row 6)
buttonPlusorminus= Button(calc_win, text="+/-", width=9, height=2, command=GetSign)
buttonPlusorminus.grid(row=6,column=0, pady=(10))
button0= Button(calc_win, text="0", width=9, height=2, command=lambda:GetNumber("0"))
button0.grid(row=6,column=1)
buttonDot= Button(calc_win, text=".", width=9, height=2, command=GetDot)
buttonDot.grid(row=6,column=2)
buttonEqual= Button(calc_win, text="=", width=9, height=2, command=Equal)
buttonEqual.grid(row=6,column=3)
calc_win.mainloop()