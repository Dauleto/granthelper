from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Checkbutton





tk = Tk()
tk.title('GRANTHELPER')
tk.geometry("550x500")
tk.config(bg="white")
tk.resizable(False, False)
# tk.iconbitmap("bomb-3175208_640.ico")

canvas = Canvas(tk, width=550, height=500, bg="gold2", highlightthickness=0)
canvas.pack()

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
    display = Label(newwin, text="Humm, see a new window !", )
    display.pack()
    chk_state = BooleanVar()
    chk_state.set(True)  # задайте проверку состояния чекбокса
    display1 = Checkbutton(newwin, text='Выбрать', var=chk_state)
    display1.pack()

    chk_state = BooleanVar()
    chk_state.set(True)  # задайте проверку состояния чекбокса
    display3 = Checkbutton(newwin, text='Выбрать', var=chk_state)
    display3.pack()
    display7 = Button(newwin, text="close", command=newwin.destroy)
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
DataEntryFrame.place(x=0, y=0, )
frontlabel = Label(DataEntryFrame, text='------Welcome to GRANT HELPER--------', width=30,font=('arial', 22, 'italic bold'), bg='gold2')
frontlabel.pack(side=TOP, expand=True)

b0 = Button(tk, text='1.ABOUT UNT', width=25, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3',activebackground='blue', relief=RIDGE,activeforeground='white', command=show_message_2)
b0.place(x=100, y=50)
b1 = Button(tk, text='2.ABOUT PROGRAM', width=25, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3',activebackground='blue', relief=RIDGE, activeforeground='white', command=start_window_1)
b1.place(x=100, y=110)
b2 = Button(tk, text='3.GOALS', width=25, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3',activebackground='blue', relief=RIDGE,activeforeground='white', command=show_message)
b2.place(x=100, y=170)
b2 = Button(tk, text='4.статистик 1', width=25, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3',activebackground='blue', relief=RIDGE,activeforeground='white', )
b2.place(x=100, y=232)
b2 = Button(tk, text='5.статистик 2', width=25, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3',activebackground='blue', relief=RIDGE,activeforeground='white', )
b2.place(x=100, y=293)
tk.mainloop()
