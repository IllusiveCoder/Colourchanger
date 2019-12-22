from tkinter import Entry, Label, Button
from tkinter import *

def go(key):
        lb.configure(bg = entry.get())

main = Tk()
main.title("Colour - Tester")
main.geometry("500x500")

button = Button(main,text = "run",relief = "flat", command =lambda: go(""))
button.place(relx = 0.75, rely = 0, relheight = 0.15, relwidth = 0.25)

entry = Entry(main, font = 30)
entry.place(relx = 0, rely = 0, relheight = 0.15, relwidth = 0.7)

lb = Label(main, bg = "white")
lb.place(relx = 0, rely = 0.20, relheight = 0.8, relwidth = 1)

entry.bind('<Return>', go)

main.mainloop()
