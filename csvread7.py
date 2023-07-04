import sys
import tkinter
import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def ButtonEvent(event):
    if tp == 0:
        EditBox5.delete(0, tkinter.END)
    elif tp == 1:
        EditBox4.delete(0, tkinter.END)
    else:
        pass
    filepath = EditBox1.get()
    SorLc = EditBox7.get()
    SorL = int(SorLc)
    Chc = EditBox2.get()
    Ch = int(Chc)
    GasNumc = EditBox3.get()
    GasNum = int(GasNumc)
    if tp == 0:
        Tempc = EditBox4.get()
        Temp = float(Tempc)
    elif tp ==1:
        Pressc = EditBox5.get()
        Press = int(Pressc)

    

root = tkinter.Tk()
root.title(u"Software Title")
root.geometry("400x400")

Static1 = tkinter.Label(text=u'test1')
Static1.pack()
Static1.place(x=100, y=200)

Static2 = tkinter.Label(text=u'test2')
Static2.pack()
Static2.place(x=100, y=300)

Static3 = tkinter.Label(text=u'file path')
Static3.pack()
Static3.place(x=50, y=-2)

Static4 = tkinter.Label(text=u'Ch')
Static4.pack()
Static4.place(x=50, y=18)

Static5 = tkinter.Label(text=u'Gass #')
Static5.pack()
Static5.place(x=50, y=37)

Static6 = tkinter.Label(text=u'Temp')
Static6.pack()
Static6.place(x=50, y=55)

Static7 = tkinter.Label(text=u'Press')
Static7.pack()
Static7.place(x=50, y=75)

Static8 = tkinter.Label(text=u'Press(0) or Temp(1)')
Static8.pack()
Static8.place(x=50, y=95)

Static9 = tkinter.Label(text=u'LP(0)/SP(1)')
Static9.pack()
Static9.place(x=50, y=115)

EditBox1 = tkinter.Entry(width=20)
EditBox1.insert(tkinter.END,"0")
EditBox1.pack()

EditBox2 = tkinter.Entry(width=20)
EditBox2.insert(tkinter.END,"0")
EditBox2.pack()

EditBox3 = tkinter.Entry(width=20)
EditBox3.insert(tkinter.END,"0")
EditBox3.pack()

EditBox4 = tkinter.Entry(width=20)
EditBox4.insert(tkinter.END,"0")
EditBox4.pack()

EditBox5 = tkinter.Entry(width=20)
EditBox5.insert(tkinter.END,"0")
EditBox5.pack()

EditBox6 = tkinter.Entry(width=20)
EditBox6.insert(tkinter.END,"0")
EditBox6.pack()

EditBox7 = tkinter.Entry(width=20)
EditBox7.insert(tkinter.END,"0")
EditBox7.pack()

Button = tkinter.Button(text=u'button')
Button.place(x=150, y=250)
Button.bind("<Button-1>",ButtonEvent)
#左クリック（<Button-1>）されると，ButtonEvent関数を呼び出すようにバインド
Button.pack()

root.mainloop()
