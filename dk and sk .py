from tkinter import *
from tkinter.ttk import Checkbutton
import csv

cod = []
profess = []

tk = Tk()
tk.title('GRANTHELPER')
tk.geometry("560x550")
tk.config(bg="white")
tk.resizable(False, False)

##--------------------------------------------ABOUT UNT-----------------------------------------------------------##
def show_message_2():
    newwin = Toplevel(tk)
    newwin.title('GRANTHELPER')
    newwin.geometry("200x300")
    newwin.resizable(0, 0)
    display = Label(newwin, text="UNT",padx=20,pady=20 )
    display.pack()
    display3 = Button(newwin, text="ABOUT UNT",padx=20,pady=35,command=unt_1)
    display3.pack()
    display4 = Button(newwin, text="UBT COUNCIL",padx=20,pady=40,command=council_1)
    display4.pack()
    display7 = Button(newwin, text="close", command=newwin.destroy)
    display7.pack()
def unt_1():
    newwin = Toplevel(tk)
    newwin.title('New Window')
    newwin.geometry("400x300")
    newwin.resizable(0, 0)

    display = Label(newwin, text="UBT also has 140 points:", )
    display.pack()

    chk_state = BooleanVar()
    chk_state.set(True)  # задайте проверку состояния чекбокса
    display1 = Checkbutton(newwin, text='history ----- 15 points', var=chk_state)
    display1.pack()

    chk_state = BooleanVar()
    chk_state.set(True)  # задайте проверку состояния чекбокса
    display2 = Checkbutton(newwin, text='grammar --- 20 points,', var=chk_state)
    display2.pack()

    chk_state = BooleanVar()
    chk_state.set(True)  # задайте проверку состояния чекбокса
    display3 = Checkbutton(newwin, text='mathematics grammar --- 15 points,', var=chk_state)
    display3.pack()

    chk_state = BooleanVar()
    chk_state.set(True)
    display4 = Checkbutton(newwin, text='Predmet 1---40,', var=chk_state)
    display4.pack()

    chk_state = BooleanVar()
    chk_state.set(True)  # задайте проверку состояния чекбокса
    display5 = Checkbutton(newwin, text='UBT can be taken 4 times. (January, March, May, June,', var=chk_state)
    display5.pack()

    chk_state = BooleanVar()
    chk_state.set(True)  # задайте проверку состояния чекбокса
    display6 = Checkbutton(newwin, text='You can win a grant from May to June,', var=chk_state)
    display6.pack()

    chk_state = BooleanVar()
    chk_state.set(True)  # задайте проверку состояния чекбокса
    display7 = Checkbutton(newwin, text='You can choose your own dates,', var=chk_state)
    display7.pack()

def council_1():
    newwin = Toplevel(tk)
    newwin.title('New Window')
    newwin.geometry("400x300")
    newwin.resizable(0, 0)
    display = Label(newwin, text="Agenda.Divide your day into three parts:", )
    display.pack()
    chk_state = BooleanVar()
    chk_state.set(True)  # задайте проверку состояния чекбокса
    display1 = Checkbutton(newwin, text='study for an exam for 8 hours a day;', var=chk_state)
    display1.pack()
    chk_state = BooleanVar()
    chk_state.set(True)  # задайте проверку состояния чекбокса
    display2 = Checkbutton(newwin, text='Exercise, relax in the fresh air, go to a disco and dance;', var=chk_state)
    display2.pack()
    chk_state = BooleanVar()
    chk_state.set(True)  # задайте проверку состояния чекбокса
    display3 = Checkbutton(newwin, text='Sleep at least 8 hours;', var=chk_state)
    display3.pack()
    display4 = Label(newwin, text="Nutrition", )
    display4.pack()
    chk_state = BooleanVar()
    chk_state = BooleanVar()
    chk_state.set(True)  # задайте проверку состояния чекбокса
    display5 = Checkbutton(newwin, text='Eat 3-4 times a day; Let the food be nutritious and rich in vitamins.', var=chk_state)
    display5.pack()
    display6 = Label(newwin, text="Place of training", )
    display6.pack()
    chk_state = BooleanVar()
    chk_state = BooleanVar()
    chk_state.set(True)  # задайте проверку состояния чекбокса
    display7 = Checkbutton(newwin, text='Prepare your workplace. Put yellow or purple objects or pictures. ', var=chk_state)
    display7.pack()
    display8 = Button(newwin, text="close", command=newwin.destroy)
    display8.pack()

##----------------------------------------------------------обой фон
DataEntryFrame = Frame(tk, bg='gold2', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=0, y=300, )
frontlabel = Label(DataEntryFrame, text='------Welcome to GRANT HELPER--------', width=30,font=('arial', 22, 'italic bold'), bg='gold2')
frontlabel.pack(side=TOP, expand=True)

b0 = Button(tk, text='1.ABOUT UNT', width=25, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3',activebackground='blue', relief=RIDGE,activeforeground='white', command=show_message_2)
b0.place(x=100, y=350)
b1 = Button(tk, text='2.ABOUT PROGRAM', width=25, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3',activebackground='blue', relief=RIDGE, activeforeground='white', )
b1.place(x=100, y=410)
b2 = Button(tk, text='3.GOALS', width=25, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3',activebackground='blue', relief=RIDGE,activeforeground='white', )
b2.place(x=100, y=470)

DataEntryFrame = Frame(tk,bg='gold2',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=0,y=0,width=560,height=300)
filepath = 'prof2.csv'
File = open(filepath)
Reader = csv.reader(File,delimiter = ';')
Data = list(Reader)
del (Data[0])

list_of_entries = []
for x in (range(0, len(Data))):
    list_of_entries.append(Data[x][0])

var = StringVar(value=list_of_entries)

listbox1 = Listbox(tk, listvariable=var,width=55)
listbox1.grid(row=0, column=0,sticky="s")

def update():
    index = listbox1.curselection()[0]
    brandlabel1.config(text=Data[index][0])
    stockpricelabel1.config(text=Data[index][1])
    countrylabel1.config(text=Data[index][2])
    datelabel1.config(text=Data[index][3])
    ssslabel1.config(text=Data[index][4])
    return None

button1 = Button(tk, text="Update", command=update)
button1.grid(row=6, column=0,)

brandlabel = Label(tk, text="Specialty").grid(row=1, column=0, sticky="w")
stockpricelabel = Label(tk, text="Number of grants").grid(row=2, column=0, sticky="w")
countrylabel = Label(tk, text="Competitors").grid(row=3, column=0, sticky="w")
datelabel = Label(tk, text="Probability").grid(row=4, column=0, sticky="w")
ssslabel = Label(tk, text="Cod").grid(row=5, column=0, sticky="w")

brandlabel1 = Label(tk, text="")
brandlabel1.grid(row=1, column=1, sticky="w")
stockpricelabel1 = Label(tk, text="")
stockpricelabel1.grid(row=2, column=1, sticky="w")
countrylabel1 = Label(tk, text="")
countrylabel1.grid(row=3, column=1, sticky="w")
datelabel1 = Label(tk, text="")
datelabel1.grid(row=4, column=1, sticky="w")
ssslabel1 = Label(tk, text="")
ssslabel1.grid(row=5, column=1, sticky="w")

tk.mainloop()
