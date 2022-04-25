from ast import Pass
import os
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk
from DataBase import LoginData
import webbrowser

def clear():
    tb1.delete(0, 'end')
    tb2.delete(0, 'end')

def VerifyData(Username,Password):
    temp = LoginData(Username,Password)
    if (temp == "success"):
        messagebox.showinfo("Message", "Login Successfull")
        top.destroy()
        os.system('python C://Roadster//DEGREE//SEMESTER4//PYTHON//Project//Home.py')
    else:
        messagebox.showwarning("Warning", "Some Error Occured")

def ExtractData():
    Username = tb1.get()
    Password = tb2.get()
    if Username == "":
        messagebox.showwarning("Warning", "Enter all Details")
    else:
        if Password == "":
            messagebox.showwarning("Warning", "Enter all Details")
        else:
            clear()
            VerifyData(Username,Password)

def callback(event):
    webbrowser.open_new_tab("https://mmt-roadster-systems.netlify.app/index.html")

def Func1(event):
    top.destroy()
    os.system('python C://Roadster//DEGREE//SEMESTER4//PYTHON//Project//Forgot.py')

def Func2(event):
    top.destroy()
    os.system('python C://Roadster//DEGREE//SEMESTER4//PYTHON//Project//SignUp.py')

top = Tk()
top.geometry("600x600+500+150")
top.resizable(0, 0)
top.title("LOGIN PAGE !!")
p1 = PhotoImage(file ="C://Roadster//DEGREE//SEMESTER4//PYTHON//Project//Icons//icont.png")
top.iconphoto(False, p1)
bg=ImageTk.PhotoImage(file="C://Roadster//DEGREE//SEMESTER4//PYTHON//Project//Icons//back.jpg")
bg_image=Label(top,image=bg).place(x=0,y=0,width=1490,height=750)
Topframe = Frame(top,bg='#041a3b',height=500,width=450).place(x=75,y=75)

t1 = Label(top,text="COVID-19 TRACKER",bg='#041a3b',fg='#ffffff',font='Times 30 bold')
t1.place(x=100,y=90)
t1.bind("<Button>", callback)

t2 = Label(Topframe,text="LOGIN HERE",bg='#041a3b',fg='#ffffff',font='Arial 20 bold').place(x=200,y=180)
t3 = Label(Topframe,text="USERNAME  :",bg='#041a3b',fg='#ffffff',font='Arial 15 bold').place(x=120,y=270)
t4 = Label(Topframe,text="PASSWORD :",bg='#041a3b',fg='#ffffff',font='Arial 15 bold').place(x=120,y=330)

tb1 = Entry(font=("Arial",15),bg='#041a3b',fg='#ffffff')
tb1.place(x=255,y=270,width=250)
tb2 = Entry(font=("Arial",15),bg='#041a3b',fg='#ffffff',show="*")
tb2.place(x=255,y=330,width=250)

b1 = Button(Topframe,text="LOG-IN",bg="#0c979c",bd=0,font=("Arial",15,"bold"),fg="white",command=ExtractData).place(x=180,y=380,width=250)

t5 = Label(Topframe,bg='#041a3b', fg="white", text="Forgot Password ?", font="Arial 10")
t5.bind("<Button>", Func1)
t5.place(x=250,y=420)

t6 = Label(Topframe,bg='#041a3b', fg="white", text="Don't Have an Account?", font="Arial 10")
t6.bind("<Button>", Func2)
t6.place(x=220,y=550)

top.mainloop()