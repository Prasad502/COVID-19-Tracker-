from asyncio.windows_events import NULL
from email import message
import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
import requests
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

api_url = "https://disease.sh/v3/covid-19/all"
response = requests.get(api_url)
response_info = response.json()
skeys = list(response_info.keys())

names = ['GLOBAL STATS', 'Cases', 'Recovered', 'Critical', 'Active', 'Today Cases', 'Deaths', 'Today Deaths','Affected Countries']
nkeys = ['cases', 'recovered', 'critical', 'active', 'todayCases', 'deaths', 'todayDeaths', 'affectedCountries']

values = ['', response_info.get('cases'), response_info.get('recovered'), response_info.get('critical'),
        response_info.get('active'), response_info.get('todayCases'), response_info.get('deaths'),
        response_info.get('todayDeaths'), response_info.get('affectedCountries')]

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def data():
    tab3line_style = ttk.Style()
    tab3line_style.configure("Line3.TSeparator", background=_from_rgb((0, 200, 244)))
    for i in range(len(names)):
        Label(frame, bg=_from_rgb((23, 29, 66)), fg=_from_rgb((0, 200, 244)), text=names[i],font="Verdana 15 bold").grid(row=i, column=1, sticky='w', padx=15, pady=10)
        Label(frame, bg=_from_rgb((23, 29, 66)), fg=_from_rgb((0, 200, 244)), text=values[i],font="Verdana 15 bold").grid(row=i, column=2, padx=280)

    for i in range(len(names) - 1):
        ttk.Separator(frame, orient='horizontal', style="Line3.TSeparator").grid(column=0, row=i, columnspan=3,sticky='ew', rowspan=2)


def quit_me():
    top.quit()
    top.destroy()

def closew():
    top.quit()
    top.destroy()
    os.system('Track_Countries.py')

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=200, height=200)

labels = ['Total Cases', 'Recovered', 'Deaths', 'Active']
share = [response_info['cases'], response_info['recovered'], response_info['deaths'], response_info['active']]

top = Tk()
top.geometry("700x660+500+150")
top.resizable(0, 0)
top.title("Covid-19 Tracker")
top.protocol("WM_DELETE_WINDOW", quit_me)

Frame_Login = Frame(top, bg=_from_rgb((2, 66, 101)))  # 23, 29, 66
Frame_Login.place(x=0, y=0, height=660, width=700)

Frame_Login1 = Frame(top, bg=_from_rgb((23, 29, 66)), highlightbackground=_from_rgb((0, 200, 244)),highlightthickness=3)  # 23, 29, 66
Frame_Login1.place(x=10, y=8, height=330, width=680)

Frame_Login2 = Frame(top, bg=_from_rgb((23, 29, 66)), highlightbackground=_from_rgb((0, 200, 244)),highlightthickness=3)  # 23, 29, 66
Frame_Login2.place(x=10, y=342, height=310, width=680)

fig = Figure(figsize=(6.6, 3), dpi=100, facecolor=_from_rgb((23, 29, 66)))  # create a figure object

ax = fig.add_subplot(111)  # add an Axes to the figure

explode = (0.05, 0.05, 0.05, 0.05)
colors = ['#FFA827', '#66BB6A', '#EE534F','#28B6F6']

# Pie Chart
ax.pie(share, colors=colors,pctdistance=0.85,explode=explode)
ax.set_position([0, 0.1, 0.8, 0.8])
lg = ax.legend(loc='center right', labels=labels, bbox_to_anchor=(1.6, 0.5), facecolor=_from_rgb((23, 29, 66)),edgecolor=_from_rgb((0, 200, 244)))

for text in lg.get_texts():
    text.set_color(_from_rgb((0, 200, 244)))

centre_circle = plt.Circle((0, 0), 0.70, fc=_from_rgb((23, 29, 66)))
figure = plt.gcf()
fig.gca().add_artist(centre_circle)

chart1 = FigureCanvasTkAgg(fig, Frame_Login1)
chart1.get_tk_widget().place(x=5, y=16)

Label(Frame_Login1, bg=_from_rgb((23, 29, 66)), fg=_from_rgb((0, 200, 244)), text="Covid-19 Tracker",font="Verdana 15 bold").place(x=250, y=15)

btn = Button(Frame_Login1,bg=_from_rgb((0, 200, 244)), text="TRACK COUNTRIES", width=7, justify=CENTER, fg=_from_rgb((23, 29, 66)), font="Verdana 12 bold", command=closew)
btn.place(height=30, width=200, x=250, y=280)

canvas = Canvas(Frame_Login2)
frame = Frame(canvas)
myscrollbar = Scrollbar(Frame_Login2, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right", fill="y")
canvas.place(x=0, y=0, width=657, height=305)
canvas.create_window((0, 0), window=frame, anchor='nw', width=657)
frame.bind("<Configure>", myfunction)
frame.configure(bg=_from_rgb((23, 29, 66)))
data()
top.mainloop()
