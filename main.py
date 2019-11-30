#!/usr/bin/env python3
from time import sleep, strftime, time
from tkinter import Tk, StringVar, ttk


def start_timer(*args):
    global start_time
    start_time = strftime('%H:%M:%S') # return current time in format HH:MM:SS
    maintime.set('Started at ' + start_time)


def close(*args):
    root.destroy()


root = Tk()

start_time = strftime('%H:%M:%S')
maintime = StringVar()

ttk.Button(root, text='start', width=17, command=start_timer).grid(row=0, column=0)
ttk.Label(root, textvariable=maintime).grid(row=1, column=0)

root.bind('<Return>', start_timer) # hit Enter to start
root.bind('<Control-Key-w>', close) # hit Ctrl-W to close window

root.mainloop()
