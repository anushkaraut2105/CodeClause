# pip install pyshorteners

import pyshorteners
from tkinter import *

win = Tk()
win.geometry("500x270")
win.configure(bg="red")
#button function
def short():
    url = entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)

    entry2.insert(END,s)
#label for entering user url
Label(win,text="Enter Your Url Link", font="impack 17 bold",bg="black",fg="white").pack(fill="x")
#Entry box
entry1 = Entry(win,font="6",bd=3,width=40)
entry1.pack(pady=20)
#Button
Button(win,text="Click me",font="impack 12 bold",bg="blue",fg="white",width="14",command=short).pack()
#Entry
entry2 = Entry(win,font="impack 16 bold",bg="red",width=24)
entry2.pack(pady=20)
mainloop()


url = input('Enter the url: ')


def shortenurl(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shortenurl(url)