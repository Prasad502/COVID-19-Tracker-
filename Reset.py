import os
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk
from DataBase import UpdatePass

def Update(Username,Pass):
    temp = UpdatePass(Username,Pass)
    if (temp == "success"):
        messagebox.showinfo("Message", "Password Updated Successfull")
        top.destroy()
        os.system('python C://Roadster//DEGREE//SEMESTER4//PYTHON//Project//login.py')
    else:
        messagebox.showwarning("Warning", "Some Error Occured")

def clear():
    tb1.delete(0, 'end')
    tb2.delete(0, 'end')
    tb3.delete(0, 'end')

def ExtractData():
    Username = tb1.get()
    Password = tb2.get()
    New_Pass = tb3.get()
    if Username == "":
        messagebox.showwarning("Warning", "Enter all Details")
    else:
        if Password == "":
            messagebox.showwarning("Warning", "Enter all Details")
        else:
            if New_Pass == "":
                messagebox.showwarning("Warning", "Enter all Details")
            else:
                if (Password != New_Pass):
                    messagebox.showwarning("Warning", "Password Mismatch")
                else:
                    clear()
                    Update(Username,Password)

top = Tk()
top.geometry("600x600+500+150")
top.resizable(0, 0)
top.title("RESET PASSWORD")
p1 = PhotoImage(file = 'C://Roadster//DEGREE//SEMESTER4//PYTHON//Project//Icons//icont.png')
top.iconphoto(False, p1)
bg=ImageTk.PhotoImage(file="C://Roadster//DEGREE//SEMESTER4//PYTHON//Project//Icons//back.jpg")
bg_image=Label(top,image=bg).place(x=0,y=0,width=1490,height=750)
Topframe = Frame(top,bg='#041a3b',height=500,width=450).place(x=75,y=75)

t1 = Label(top,text="COVID-19 TRACKER",bg='#041a3b',fg='#ffffff',font='Times 30 bold').place(x=100,y=90)
t2 = Label(Topframe,text="RESET PASSWORD",bg='#041a3b',fg='#ffffff',font='Arial 20 bold').place(x=200,y=180)
t3 = Label(Topframe,text="USERNAME  :",bg='#041a3b',fg='#ffffff',font='Arial 15 bold').place(x=90,y=270)
t4 = Label(Topframe,text="NEW PASSWORD :",bg='#041a3b',fg='#ffffff',font='Arial 15 bold').place(x=90,y=330)
t5 = Label(Topframe,text="NEW PASSWORD :",bg='#041a3b',fg='#ffffff',font='Arial 15 bold').place(x=90,y=390)

tb1 = Entry(font=("Arial",15),bg='#041a3b',fg='#ffffff')
tb1.place(x=285,y=270,width=200)
tb2 = Entry(font=("Arial",15),bg='#041a3b',fg='#ffffff',show="*")
tb2.place(x=285,y=330,width=200)
tb3 = Entry(font=("Arial",15),bg='#041a3b',fg='#ffffff',show="*")
tb3.place(x=285,y=390,width=200)

b1 = Button(Topframe,text="RESET PASSWORD",bg="#0c979c",bd=0,font=("Arial",15,"bold"),fg="white",command=ExtractData).place(x=180,y=470,width=250)

top.mainloop()