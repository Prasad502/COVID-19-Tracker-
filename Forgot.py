import os
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk
from email.message import EmailMessage
import smtplib
import random

temp = random.randint(0,999999)

def clear():
    tb1.delete(0, 'end')
    tb2.delete(0, 'end')

def NextWindow():
    top.destroy()
    os.system('python C://Roadster//DEGREE//SEMESTER4//PYTHON//Project//Reset.py')

def ResetPass():
    Email = tb1.get()
    msg = EmailMessage()
    msg.set_content("Hello , \n One Time Password for your account is : " + str(temp))
    msg['subject'] = "Password recovery."
    msg['from'] = "ROADSTR SYSTEMS"
    msg['to'] = Email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("digitalchamp2016@gmail.com", "QAZWSXEDCRFV@109")
    server.send_message(msg)
    clear()
    messagebox.showinfo("Message", "OTP sent Successfully!")

def verifyOTP():
    print(temp)
    OTP = int(tb2.get())
    if (OTP == temp):
        NextWindow()
    else:
        messagebox.showwarning("Warning", "Invalid OTP")


top = Tk()
top.geometry("600x600+500+150")
top.resizable(0, 0)
top.title("PASSWORD RESET")
p1 = PhotoImage(file = 'C://Roadster//DEGREE//SEMESTER4//PYTHON//Project//Icons//icont.png')
top.iconphoto(False, p1)
bg=ImageTk.PhotoImage(file="C://Roadster//DEGREE//SEMESTER4//PYTHON//Project//Icons//back.jpg")
bg_image=Label(top,image=bg).place(x=0,y=0,width=1490,height=750)
Topframe = Frame(top,bg='#041a3b',height=500,width=450).place(x=75,y=75)

t1 = Label(top,text="COVID-19 TRACKER",bg='#041a3b',fg='#ffffff',font='Times 30 bold').place(x=100,y=90)

t2 = Label(Topframe,text="RESET PASSWORD",bg='#041a3b',fg='#ffffff',font='Arial 20 bold').place(x=200,y=180)
t3 = Label(Topframe,text="EMAIL-ID  :",bg='#041a3b',fg='#ffffff',font='Arial 15 bold').place(x=120,y=270)
t4 = Label(Topframe,text="OTP :",bg='#041a3b',fg='#ffffff',font='Arial 15 bold').place(x=120,y=400)


tb1 = Entry(font=("Arial",15),bg='#041a3b',fg='#ffffff')
tb1.place(x=255,y=270,width=250)
tb2 = Entry(font=("Arial",15),bg='#041a3b',fg='#ffffff')
tb2.place(x=255,y=400,width=250)

b1 = Button(Topframe,text="Get OTP",bg="#0c979c",bd=0,font=("Arial",15,"bold"),fg="white",command=ResetPass).place(x=180,y=320,width=250)
b2 = Button(Topframe,text="Reset Password",bg="#0c979c",bd=0,font=("Arial",15,"bold"),fg="white",command=verifyOTP).place(x=180,y=450,width=250)

top.mainloop()

