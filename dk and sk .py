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
##--------------------------------------------ABOUT PROGRAM-----------------------------------------------------------##
def start_window_1():
    newwin = Toplevel(tk)
    newwin.title('GRANTHELPER')
    newwin.geometry("220x200")
    newwin.resizable(0, 0)
    display1 = Label(newwin, text="QUESTION",)
    display1.pack()
    display2 = Button(newwin, text="Question 1",command=question_1)
    display2.pack()
    display3 = Button(newwin, text="Question 2",command=question_2)
    display3.pack()
    display4 = Button(newwin, text="Question 3",command=question_3)
    display4.pack()
    display5 = Button(newwin, text="Question 4",command=question_4)
    display5.pack()
    display7= Button(newwin,text="close",command=newwin.destroy)
    display7.pack()
def question_1():
        newwin = Toplevel(tk)
        newwin.title('New Window')
        newwin.geometry("400x200")
        newwin.resizable(0, 0)
        display = Label(newwin, text="Why did we invent this programme?", )
        display.pack()
        display1 = Label(newwin, text="First of all, thank you all.Today we are going to talk a little bit about the", )
        display1.pack()
        display2 = Label(newwin, text="the programme, because we invented this programme,because we want ", )
        display2.pack()
        display3 = Label(newwin, text="to help at least one person. Because everyone who goes to UBT and wants ", )
        display3.pack()
        display4 = Label(newwin, text="to win a grant has fear and mistrust.For accessing and using our software.", )
        display4.pack()
        display5 = Label(newwin, text="And this programme will show you everything with digital evidence and", )
        display5.pack()
        display6 = Label(newwin, text="calm your worries.We are happy that the programme will benefit ", )
        display6.pack()
        display7 = Label(newwin, text="your future professional", )
        display7.pack()
        display8 = Button(newwin, text="exit", command=newwin.destroy)
        display8.pack()
def question_2():
    newwin = Toplevel(tk)
    newwin.title('New Window')
    newwin.geometry("400x130")
    newwin.resizable(0, 0)
    display = Label(newwin, text="What are the benefits of the programme?", )
    display.pack()
    display1 = Label(newwin, text="The biggest advantage of the programme is the availability of accurate", )
    display1.pack()
    display2 = Label(newwin,text="information.Our programme is free and there are no unnecessary", )
    display2.pack()
    display3 = Label(newwin,text="  advertisements 😁", )
    display3.pack()
    display4 = Button(newwin, text="exit", command=newwin.destroy)
    display4.pack()
def question_3():
        newwin = Toplevel(tk)
        newwin.title('New Window')
        newwin.geometry("400x150")
        newwin.resizable(0, 0)
        display = Label(newwin, text="What is the purpose of the programme?", )
        display.pack()
        display1 = Label(newwin, text="The purpose of the programme is for you to:", )
        display1.pack()
        display1 = Label(newwin,text="1. To choose a profession,", )
        display1.pack()
        display1 = Label(newwin,text="2. To prepare for the UNT,", )
        display1.pack()
        display1 = Label(newwin,text="3. To choose a university,", )
        display1.pack()
        display1 = Label(newwin,text="4. Helps to be confident.", )
        display1.pack()
        display2 = Button(newwin, text="exit", command=newwin.destroy)
        display2.pack()
def question_4():
        newwin = Toplevel(tk)
        newwin.title('New Window')
        newwin.geometry("420x100")
        newwin.resizable(0, 0)
        display = Label(newwin, text="Is the programme bad for you?", )
        display.pack()
        display1 = Label(newwin, text="We consider the programme harmless because all the information is correct.", )
        display1.pack()
        display2 = Button(newwin, text="exit", command=newwin.destroy)
        display2.pack()
##--------------------------------------------GOALS-----------------------------------------------------------##
def show_message():
    newwin = Tk()
    newwin.title('GRANTHELPER')
    newwin.geometry("300x250")
    newwin.resizable(0, 0)
    display1 = Label(newwin, text="What profession you want to choose?", )
    display1.pack()
    message = StringVar()
    display2 = Entry(newwin, textvariable=message, )
    display2.pack()
    display3 = Label(newwin, text="In what university you want to study?", )
    display3.pack()
    message = StringVar()
    display4 = Entry(newwin, textvariable=message, )
    display4.pack()
    display5 = Label(newwin, text="How many points you want to earn in UNT?", )
    display5.pack()
    message = StringVar()
    display6 = Entry(newwin, textvariable=message, )
    display6.pack()
    display7 = Label(newwin, text="Do you believe on yourself?", )
    display7.pack()
    message = StringVar()
    display8 = Entry(newwin, textvariable=message, )
    display8.pack()
    display9 = Button(newwin, text="Read the answer carefully.", command=clicked)
    display9.pack()
    display10 = Button(newwin, text="close", command=newwin.destroy)
    display10.pack()
def clicked():
    window = Tk()
    window.title('GRANTHELPER')
    display1 = Button(window, text="You are good at everything, you will achieve your goals.", command=clicked,bg="black", fg="gold2")
    display1.pack()

##----------------------------------------------------------обой фон
DataEntryFrame = Frame(tk, bg='gold2', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=0, y=300, )
frontlabel = Label(DataEntryFrame, text='------Welcome to GRANT HELPER--------', width=30,font=('arial', 22, 'italic bold'), bg='gold2')
frontlabel.pack(side=TOP, expand=True)

b0 = Button(tk, text='1.ABOUT UNT', width=25, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3',activebackground='blue', relief=RIDGE,activeforeground='white', command=show_message_2)
b0.place(x=100, y=350)
b1 = Button(tk, text='2.ABOUT PROGRAM', width=25, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3',activebackground='blue', relief=RIDGE, activeforeground='white',command=start_window_1 )
b1.place(x=100, y=410)
b2 = Button(tk, text='3.GOALS', width=25, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3',activebackground='blue', relief=RIDGE,activeforeground='white', command=show_message)
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
