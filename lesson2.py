from tkinter import *


def change():
    if w.get() == 0:
        label['bg'] = 'red'
    elif w.get() == 1:
        label['bg'] = 'green'
    elif w.get() == 2:
        label['bg'] = 'yellow'


window = Tk()

w = IntVar()
w.set(0)

red = Radiobutton(text="Червоний", variable=w, value=0)
red.pack()
green = Radiobutton(text="Зелений", variable=w, value=1)
green.pack()
yellow = Radiobutton(text="Жовтий", variable=w, value=2)
yellow.pack()

changebutton = Button(text="Змінити", command=change)
changebutton.pack()

label = Label(width=20, height=10)
label.pack()

window.mainloop()
