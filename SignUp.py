from ast import Num
import os
from tkinter import messagebox
from tkinter import *
from tokenize import Number
from PIL import ImageTk
import re
from DataBase import SignupData

def clear():
    tb1.delete(0, 'end')
    tb2.delete(0, 'end')
    tb3.delete(0, 'end')
    tb4.delete(0, 'end')

def InsertToDB(Username,Password,Number,Email):
    temp = SignupData(Username,Password,Number,Email)
    if (temp == "success"):
        messagebox.showinfo("Message", "Sign-Up Successfull")
        top.destroy()
        os.system('python C://Roadster//DEGREE//SEMESTER4//PYTHON//Project//login.py')
    else:
        messagebox.showwarning("Warning", "Some Error Occured")

def isValid(s): 
    if (s.isdigit()):
        Pattern = re.compile("[0-9]{10}")
        return Pattern.match(s)
    else:
        return False
    
    
def back(event):
    top.destroy()
    os.system('python C://Roadster//DEGREE//SEMESTER4//PYTHON//Project//login.py')

def ExtractData():
    Username = tb1.get()
    Password = tb2.get()
    Number = tb3.get()
    Email = tb4.get()
    if Username == "":
        messagebox.showwarning("Warning", "Enter all Details")
    else:
        if Password == "":
            messagebox.showwarning("Warning", "Enter all Details")
        else:
            if Number == "":
                messagebox.showwarning("Warning", "Enter all Details")
            else:
                if Email == "" :
                    messagebox.showwarning("Warning", "Enter all Details")
                else:
                    if not re.search("@",Email):
                        messagebox.showwarning("Warning", "Invalid email")
                    elif re.search("[-+_!#$%^&*()<>?/\|}{~:]", Email):
                        messagebox.showwarning("Warning", "Invalid email")
                    else: 
                        if len(Number) > 10 or len(Number) < 10:
                            messagebox.showwarning("Warning", "Enter valid Number")
                        else:
                            if (isValid(Number)):
                                clear()
                                InsertToDB(Username,Password,Number,Email)
                            else:
                                messagebox.showwarning("Warning", "Enter valid Number")
                            


top = Tk()
top.geometry("600x600+500+150")
top.resizable(0, 0)
top.title("SIGN-UP PAGE !!")
p1 = PhotoImage(file = 'C://Roadster//DEGREE//SEMESTER4//PYTHON//Project//Icons//icont.png')
top.iconphoto(False, p1)
bg=ImageTk.PhotoImage(file="C://Roadster//DEGREE//SEMESTER4//PYTHON//Project//Icons//back.jpg")
bg_image=Label(top,image=bg).place(x=0,y=0,width=1490,height=750)
Topframe = Frame(top,bg='#041a3b',height=500,width=450).place(x=75,y=75)

t1 = Label(top,text="COVID-19 TRACKER",bg='#041a3b',fg='#ffffff',font='Times 30 bold').place(x=100,y=90)
t2 = Label(Topframe,text="SIGN-UP HERE",bg='#041a3b',fg='#ffffff',font='Arial 20 bold').place(x=200,y=180)
t3 = Label(Topframe,text="USERNAME  :",bg='#041a3b',fg='#ffffff',font='Arial 15 bold').place(x=120,y=270)
t4 = Label(Topframe,text="PASSWORD :",bg='#041a3b',fg='#ffffff',font='Arial 15 bold').place(x=120,y=330)
t5 = Label(Topframe,text="PHONE NO. :",bg='#041a3b',fg='#ffffff',font='Arial 15 bold').place(x=120,y=390)
t6 = Label(Topframe,text="EMAIL-ID :",bg='#041a3b',fg='#ffffff',font='Arial 15 bold').place(x=120,y=450)

tb1 = Entry(font=("Arial",15),bg='#041a3b',fg='#ffffff')
tb1.place(x=255,y=270,width=250)
tb2 = Entry(font=("Arial",15),bg='#041a3b',fg='#ffffff',show="*")
tb2.place(x=255,y=330,width=250)
tb3 = Entry(font=("Arial",15),bg='#041a3b',fg='#ffffff')
tb3.place(x=255,y=390,width=250)
tb4 = Entry(font=("Arial",15),bg='#041a3b',fg='#ffffff')
tb4.place(x=255,y=450,width=250)

b1 = Button(Topframe,text="SIGN-UP",bg="#0c979c",bd=0,font=("Arial",15,"bold"),fg="white",command=ExtractData).place(x=180,y=500,width=250)

logo = ImageTk.PhotoImage(file="back.png")
l1 = Label(Topframe, image=logo, bg="#0c979c")
l1.bind("<Button>", back)
l1.place(x=10, y=12)

top.mainloop()