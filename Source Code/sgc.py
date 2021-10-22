from tkinter import *
from tkinter import messagebox
import math
from idlelib.tooltip import Hovertip
from decimal import Decimal
import os
import sys
import re
################################################################################
#Functionality
#Initial Variables
Num1 = ""
Num2 = ""
OpCar = ""
First = True
res = ""
sign = "positive"
Acum = ""
size_calcwin = ""
width_calcwin = ""
height_calcwin = ""
Buttonwidthx1 = ""
Buttonwidthx2 = ""
ButtonHeight = ""
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
#Saving Numbers, First or Second
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
        screen_calc.configure(text=str(Num2))
#Operation Characters: +, -, /, x
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
#Operation Characters: square and square root
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
#Delete a character
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
#Clear all
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
#Add a dot to the operation
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
#Change the sign of the current number
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
#Settings protocol
def OpenSettings():
    buttonSettings.configure(state= DISABLED)
    def SaveSettings():
        #Calculator window changes
        global size_calcwin
        global height_calcwin
        global width_calcwin
        global Buttonwidthx1
        global Buttonwidthx2
        global ButtonHeight
        height_calcwin = entertext_height.get()
        width_calcwin = entertext_width.get()
        Buttonwidthx1 = entertext_width_buttonx1.get()
        Buttonwidthx2 = entertext_width_buttonx2.get()
        ButtonHeight = entertext_height_button.get()
        size_calcwin = str(str(width_calcwin)+"x"+str(height_calcwin))
        #Save to txt
        file = open(resource_path("settings.txt"),"r+")
        file.truncate(0)
        file.close()
        contenido = open(resource_path("settings.txt")).read().splitlines()
        contenido.insert(0,"#Calculator window settings")
        contenido.insert(1,("Height = "+str(height_calcwin)))
        contenido.insert(2,("Width = "+str(width_calcwin)))
        contenido.insert(3,("ButtonxOneWidth = "+str(Buttonwidthx1)))
        contenido.insert(4,("ButtonxTwoWidth = "+str(Buttonwidthx2)))
        contenido.insert(5,("ButtonsHeight  = "+str(ButtonHeight)))
        f = open(resource_path("settings.txt"), "w")
        f.writelines("\n".join(contenido))
        f.close
        settings_win.destroy()
        calc_win.destroy()
    global width_calcwin
    global height_calcwin
    global Buttonwidthx2
    global Buttonwidthx1
    global ButtonHeight
    GetCE()
    #Settings GUI
    settings_win = Tk()
    def on_closing():
        if messagebox.askokcancel("Exit", "Exit without aplying changes?"):
            buttonSettings.configure(state= NORMAL)
            settings_win.destroy()
    settings_win.protocol("WM_DELETE_WINDOW", on_closing)
    settings_win.geometry("250x450")
    settings_win.resizable(True, True)
    settings_win.title("Settings")
    settings_win.iconbitmap(resource_path("windowIcon.ico"))
    settings_win.configure(bg="gray20")
    labeltitle1 = Label(settings_win, text="Calculator Window Settings", width="25")
    labeltitle1.pack(pady=2)
    labelwidth = Label(settings_win, text="Width: ", width="12")
    labelwidth.pack(pady=2)
    entertext_width = Entry(settings_win, width = "12")
    entertext_width.insert(0, width_calcwin)
    entertext_width.pack(pady=2)
    labelheight = Label(settings_win, text="Height: ", width="12")
    labelheight.pack(pady=2)
    entertext_height = Entry(settings_win, width = "12")
    entertext_height.insert(0, height_calcwin)
    entertext_height.pack(pady=2)
    labeltitle1_1 = Label(settings_win, text="Calculator Buttons Settings", width="25")
    labeltitle1_1.pack(pady=2)
    labeltitle1_1_1 = Label(settings_win, text="Button x1 Width", width="18")
    labeltitle1_1_1.pack(pady=2)
    labelwidth_buttonx1 = Label(settings_win, text="Width: ", width="12")
    labelwidth_buttonx1.pack(pady=2)
    entertext_width_buttonx1 = Entry(settings_win, width = "12")
    entertext_width_buttonx1.insert(0, Buttonwidthx1)
    entertext_width_buttonx1.pack(pady=2)
    labeltitle1_1_2 = Label(settings_win, text="Button x2 Width", width="18")
    labeltitle1_1_2.pack(pady=2)
    labelwidth_buttonx2 = Label(settings_win, text="Width: ", width="12")
    labelwidth_buttonx2.pack(pady=2)
    entertext_width_buttonx2 = Entry(settings_win, width = "12")
    entertext_width_buttonx2.insert(0, Buttonwidthx2)
    entertext_width_buttonx2.pack(pady=2)
    labeltitle1_1_2 = Label(settings_win, text="Buttons Height", width="18")
    labeltitle1_1_2.pack(pady=2)
    labelheight_button = Label(settings_win, text="Height: ", width="12")
    labelheight_button.pack(pady=2)
    entertext_height_button = Entry(settings_win, width = "12")
    entertext_height_button.insert(0, ButtonHeight)
    entertext_height_button.pack(pady=10)
    buttonSave = Button(settings_win, text="Save and exit", width=25, height=1, command=SaveSettings)
    buttonSave.pack(pady=2)
    buttonSave = Button(settings_win, text="Restore defaults", width=25, height=1, command=reset_default_config)
    buttonSave.pack(pady=2)
    settings_win.mainloop()
#Get settings parameters
def Get_Calcwin_sizes():
    global size_calcwin
    global height_calcwin
    global width_calcwin
    global Buttonwidthx1
    global Buttonwidthx2
    global ButtonHeight
    print(str(resource_path("settings.txt")))
    with open(resource_path("settings.txt")) as f:
        size_list = f.readlines()[1:6]
    f.close
    height_calcwin = size_list[0]
    width_calcwin = size_list[1]
    Buttonwidthx1 = size_list[2]
    Buttonwidthx2 = size_list[3]
    ButtonHeight = size_list[4]
    height_calcwin = re.sub("[A-Za-z]","",height_calcwin)
    width_calcwin = re.sub("[A-Za-z]","",width_calcwin)
    height_calcwin = re.sub("[\n]","",height_calcwin)
    width_calcwin = re.sub("[\n]","",width_calcwin)
    height_calcwin = re.sub("[= ]","",height_calcwin)
    width_calcwin = re.sub("[= ]","",width_calcwin)
    size_calcwin = str(str(width_calcwin)+"x"+str(height_calcwin))
    Buttonwidthx1 = re.sub("[A-Za-z]","",Buttonwidthx1)
    Buttonwidthx1 = re.sub("[\n]","",Buttonwidthx1)
    Buttonwidthx1 = re.sub("[= ]","",Buttonwidthx1)
    Buttonwidthx2 = re.sub("[A-Za-z]","",Buttonwidthx2)
    Buttonwidthx2 = re.sub("[\n]","",Buttonwidthx2)
    Buttonwidthx2 = re.sub("[= ]","",Buttonwidthx2)
    ButtonHeight = re.sub("[A-Za-z]","",ButtonHeight)
    ButtonHeight = re.sub("[\n]","",ButtonHeight)
    ButtonHeight = re.sub("[= ]","",ButtonHeight)
    print(height_calcwin)
    print(width_calcwin)
    print (size_calcwin)
    print(Buttonwidthx1)
    print(Buttonwidthx2)
    print(ButtonHeight)
def reset_default_config():
    config_file = open(resource_path("settings.txt"), "w")
    config_file.truncate()
    config_file.close()
    default_config_list = ["#Calculator window settings\n","Height = 480\n", "Width = 300\n", "ButtonxOneWidth = 9\n", "ButtonxTwoWidth = 18\n", "ButtonsHeight  = 2\n"]
    config_file = open(resource_path("settings.txt"), "w")
    for config in default_config_list:
        config_file.write(config)
    config_file.close()
    sys.exit()
#################################################################################
#GUI
#Window config
calc_win = Tk()
Get_Calcwin_sizes()
calc_win.geometry(size_calcwin)
calc_win.resizable(True, True)
calc_win.title("Simple GUI Calculator")
calc_win.iconbitmap(resource_path("windowIcon.ico"))
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
buttonClear= Button(calc_win, text="CE", width=Buttonwidthx2, height=ButtonHeight, command=GetCE)
buttonClear.grid(row=2, column = 0, columnspan=2)
buttonDelete= Button(calc_win, text="DEL", width=Buttonwidthx2, height=ButtonHeight, command=GetDel)
buttonDelete.grid(row=2, column = 2, columnspan=2)
#Square, square root and division (Row 3)
buttonSquare= Button(calc_win, text="X^2", width=Buttonwidthx1, height=ButtonHeight, command=lambda:GetOpDiferent("^"))
buttonSquare.grid(row=3, column = 0, pady=(10))
buttonRoot= Button(calc_win, text="√X", width=Buttonwidthx1, height=ButtonHeight, command=lambda:GetOpDiferent("root"))
buttonRoot.grid(row=3, column = 1)
buttonDiv= Button(calc_win, text="/", width=Buttonwidthx2, height=ButtonHeight, command=lambda:GetOpNormal("/"))
buttonDiv.grid(row=3, column = 2, columnspan=2)
#7, 8, 9 and multiplication (Row 4)
button7= Button(calc_win, text="7", width=Buttonwidthx1, height=ButtonHeight, command=lambda:GetNumber("7"))
button7.grid(row=4,column=0, pady=(10))
button8= Button(calc_win, text="8", width=Buttonwidthx1, height=ButtonHeight, command=lambda:GetNumber("8"))
button8.grid(row=4,column=1)
button9= Button(calc_win, text="9", width=Buttonwidthx1, height=ButtonHeight, command=lambda:GetNumber("9"))
button9.grid(row=4,column=2)
buttonMult= Button(calc_win, text="X", width=Buttonwidthx1, height=ButtonHeight, command=lambda:GetOpNormal("x"))
buttonMult.grid(row=4,column=3)
#4, 5, 6 and Subtraction (Row 5)
button4= Button(calc_win, text="4", width=Buttonwidthx1, height=ButtonHeight, command=lambda:GetNumber("4"))
button4.grid(row=5,column=0, pady=(10))
button5= Button(calc_win, text="5", width=Buttonwidthx1, height=ButtonHeight, command=lambda:GetNumber("5"))
button5.grid(row=5,column=1)
button6= Button(calc_win, text="6", width=Buttonwidthx1, height=ButtonHeight, command=lambda:GetNumber("6"))
button6.grid(row=5,column=2)
buttonSub= Button(calc_win, text="-", width=Buttonwidthx1, height=ButtonHeight, command=lambda:GetOpNormal("-"))
buttonSub.grid(row=5,column=3)
#1, 2, 3 and Add (Row 6)
button1= Button(calc_win, text="1", width=Buttonwidthx1, height=ButtonHeight, command=lambda:GetNumber("1"))
button1.grid(row=6,column=0, pady=(10))
button2= Button(calc_win, text="2", width=Buttonwidthx1, height=ButtonHeight, command=lambda:GetNumber("2"))
button2.grid(row=6,column=1)
button3= Button(calc_win, text="3", width=Buttonwidthx1, height=ButtonHeight, command=lambda:GetNumber("3"))
button3.grid(row=6,column=2)
buttonAdd= Button(calc_win, text="+", width=Buttonwidthx1, height=ButtonHeight, command=lambda:GetOpNormal("+"))
buttonAdd.grid(row=6,column=3)
#+/-, 0, . and Equal (Row 7)
buttonPlusorminus= Button(calc_win, text="+/-", width=Buttonwidthx1, height=ButtonHeight, command=GetSign)
buttonPlusorminus.grid(row=7,column=0, pady=(10))
button0= Button(calc_win, text="0", width=Buttonwidthx1, height=ButtonHeight, command=lambda:GetNumber("0"))
button0.grid(row=7,column=1)
buttonDot= Button(calc_win, text=".", width=Buttonwidthx1, height=ButtonHeight, command=GetDot)
buttonDot.grid(row=7,column=2)
buttonEqual= Button(calc_win, text="=", width=Buttonwidthx1, height=ButtonHeight, command=Equal)
buttonEqual.grid(row=7,column=3)
#info
info_label = Label(calc_win, text="Baskerville Inc. SH. v1.3", width=21, height=1, bg="gray", anchor="w", fg="white")
info_label.grid(row=8, columnspan=4, column=0)
##########################################
#Key Bindings and Hover tips
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
