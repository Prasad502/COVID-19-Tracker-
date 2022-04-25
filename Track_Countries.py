import os
import urllib
from tkinter import *
import io
from tkinter import ttk
import requests
from PIL import Image, ImageTk
import tkinter as tk
from urllib.request import urlopen

api_url = "https://corona.lmao.ninja/v2/countries"
response = requests.get(api_url)
response_info = response.json()

global counter
counter = 1

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=200, height=200)

def logout(event):
    top.destroy()
    os.system('python C://Roadster//DEGREE//SEMESTER4//PYTHON//Project//login.py')
    
def back(event):
    top.destroy()
    os.system('Home.py')


def data():
    tab3line_style = ttk.Style()
    tab3line_style.configure("Line3.TSeparator", background=_from_rgb((0, 200, 244)))
    for i in range(len(response_info)):
        r = response_info[i]['countryInfo']['flag']
        page = urllib.request.Request(r, headers={'User-Agent': 'Mozilla/5.0'})
        my_page = urlopen(page)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        pil_img.thumbnail((50, 50), Image.ANTIALIAS)
        tk_img = ImageTk.PhotoImage(pil_img)
        l1 = Label(frame, image=tk_img, font="Verdana 15 bold")
        l1.grid(row=i, column=1, sticky='w', padx=15, pady=10)
        l1.dontlooseit = tk_img
        l1 = Label(frame, bg=_from_rgb((23, 29, 66)), fg=_from_rgb((0, 200, 244)), text=response_info[i]['country'], font = "Verdana 15 bold")
        temp = i
        l1.bind("<Button-1>", lambda event, arg=temp: on_focus_out(event, arg))
        l1.grid(row=i, column=2, padx=100)
    for i in range(len(response_info) - 1):
        ttk.Separator(frame, orient='horizontal', style="Line3.TSeparator").grid(column=0, row=i, columnspan=5,sticky='ew', rowspan=2)


def on_closing(window):
    global counter
    window.destroy()
    counter -= 1


def on_focus_out(event, arg):
    global counter
    if counter < 2:
        #print(event.widget['text'], arg)
        attributes = ['Country', 'Cases', 'Today Cases', 'Deaths', 'Today Deaths', 'Recovered', 'Active', 'Critical']
        values = [response_info[arg].get('country'), response_info[arg].get('cases'), response_info[arg].get('todayCases'),
                response_info[arg].get('Deaths'), response_info[arg].get('todayDeaths'),
                response_info[arg].get('recovered'), response_info[arg].get('active'), response_info[arg].get('critical')]
        #print(values)

        win = Tk()
        win.geometry("400x600+500+150")
        win.resizable(0, 0)
        win.title("Covid-19 Tracker")
        win.protocol("WM_DELETE_WINDOW", lambda x=win: on_closing(x))

        Frame_Login = Frame(win, bg=_from_rgb((2, 66, 101)))  # 23, 29, 66
        Frame_Login.place(x=0, y=0, height=600, width=400)

        Frame_Login1 = Frame(Frame_Login, bg=_from_rgb((23, 29, 66)), highlightbackground=_from_rgb((0, 200, 244)),highlightthickness=3)  # 23, 29, 66
        Frame_Login1.place(x=10, y=58, height=520, width=380)

        Label(Frame_Login, bg=_from_rgb((2, 66, 101)), fg=_from_rgb((0, 200, 244)), text="Details of Affected Country",font="Verdana 15 bold").place(x=45, y=15)

        tab3line_style = ttk.Style()
        tab3line_style.configure("Line3.TSeparator", background=_from_rgb((0, 200, 244)))
        for i in range(len(attributes)):
            Label(Frame_Login1, bg=_from_rgb((23, 29, 66)), fg=_from_rgb((0, 200, 244)), text=attributes[i],font="Verdana 15 bold").grid(row=i, column=1, sticky='w', padx=15, pady=10)
            Label(Frame_Login1, bg=_from_rgb((23, 29, 66)), fg=_from_rgb((0, 200, 244)), text=values[i],font="Verdana 15 bold").grid(row=i, column=2, padx=20)

        counter += 1

top = Tk()
top.geometry("700x660+330+18")
top.resizable(0, 0)
top.title("Covid-19 Tracker")

Frame_Login = Frame(top, bg=_from_rgb((2, 66, 101)))  # 23, 29, 66
Frame_Login.place(x=0, y=0, height=660, width=700)

Frame_Login2 = Frame(Frame_Login, bg=_from_rgb((23, 29, 66)), highlightbackground=_from_rgb((0, 200, 244)),highlightthickness=3)  # 23, 29, 66
Frame_Login2.place(x=10, y=70, height=580, width=680)

Label(Frame_Login, bg=_from_rgb((2, 66, 101)), fg=_from_rgb((0, 200, 244)), text="Affected Countries",font="Verdana 15 bold").place(x=245, y=15)

logo = ImageTk.PhotoImage(file="back.png")
l1 = Label(Frame_Login, image=logo, bg=_from_rgb((2, 66, 101)))
l1.bind("<Button>", back)
l1.place(x=10, y=12)

logo1 = ImageTk.PhotoImage(file="C://Roadster//DEGREE//SEMESTER4//PYTHON//Project//Icons//logout.png")
l2 = Label(Frame_Login, image=logo1, bg=_from_rgb((2, 66, 101)))
l2.bind("<Button>", logout)
l2.place(x=650, y=15)

canvas = Canvas(Frame_Login2)
frame = Frame(canvas)
myscrollbar = Scrollbar(Frame_Login2, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right", fill="y")
canvas.place(x=0, y=0, width=657, height=574)
canvas.configure(bg=_from_rgb((23, 29, 66)))
canvas.create_window((0, 0), window=frame, anchor='nw', width=657)
frame.bind("<Configure>", myfunction)
frame.configure(bg=_from_rgb((23, 29, 66)))
data()
top.mainloop()
