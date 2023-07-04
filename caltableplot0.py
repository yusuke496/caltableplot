import sys
import tkinter
import pandas as pd
import matplotlib
import numpy as np
from numpy import convolve
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import re
from statistics import mean

def rownum_culc(a,b):
    return int((a+0.1)/0.02)*168+int((b-18)/2)*12+10
def colnum_culc(c,d,e):
    return c*20+d*5+e
def ButtonEvent(event):

    tp = var1.get()
    SorL = var2.get()
    filepath = EditBox1.get()
    filepath = "caltable_data/"+filepath

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

    data=[]
    datagf=[]

#get data
    for i in range(0,14):
        Press=2*i+18
        RowNum=rownum_culc(Temp,Press)
        ColNum=colnum_culc(SorL,Ch,GasNum)
        csvdata = pd.read_csv(filepath, header=None)
        databf=np.array(csvdata.values[RowNum:RowNum+12,ColNum])
        #print(databf[0])
        data.append(databf)
        i=i+1
#plot data
    xlist = [ 2*i+18 for i in range(14) ]
    #xlist = [ i*0.02-1 for i in range(11) ]
    ylist=[1,2,3,4,5,6,7,8,9,10,11,12]

    X, Y = np.meshgrid(np.array(xlist), np.array(ylist))
    Z = np.array(data)
    print(Z)
    #sys.exit()
    fig = plt.figure(figsize=(6,4))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel("data points")
    ax.set_ylabel("time (min)")
    ax.set_zlabel("abs")
    surf=ax.plot_wireframe(X, Y, Z, color='blue',linewidth=0.2)
    fig.show()

root = tkinter.Tk()
root.title("Calibration Table 14")
root.geometry("400x200")

# チェックボックスの各項目の初期値
#Val1 = tkinter.BooleanVar()
#Val2 = tkinter.BooleanVar()

#Val1.set(False)
#Val2.set(False)

#CheckBox1 = tkinter.Checkbutton(text="Temp: check, Press: do not check", variable=Val1)
#CheckBox1.place(x=145, y=20)

#CheckBox2 = tkinter.Checkbutton(text="SP: check, LP: do not check", variable=Val2)
#CheckBox2.place(x=145, y=40)

# ラジオボタン

var1 = tkinter.IntVar()
var1.set(0)

var2 = tkinter.IntVar()
var2.set(0)

rdo1 = tkinter.Radiobutton(root, value=0, variable=var1, text='Pressure')
rdo1.place(x=100, y=30)

rdo2 = tkinter.Radiobutton(root, value=1, variable=var1, text='Temparature')
rdo2.place(x=100, y=50)

# ラジオボタン
rdo3 = tkinter.Radiobutton(root, value=0, variable=var2, text='Long path')
rdo3.place(x=250, y=30)

rdo4 = tkinter.Radiobutton(root, value=1, variable=var2, text='Short path')
rdo4.place(x=250, y=50)

Static3 = tkinter.Label(text='file path')
Static3.pack()
Static3.place(x=20, y=10)

Static4 = tkinter.Label(text='Ch (0~3)')
Static4.pack()
Static4.place(x=20, y=90)

Static5 = tkinter.Label(text='Gass # (0~4)')
Static5.pack()
Static5.place(x=20, y=110)

Static6 = tkinter.Label(text='Temp (-0.1~0.1)')
Static6.pack()
Static6.place(x=20, y=130)

Static7 = tkinter.Label(text='Press (18~44)')
Static7.pack()
Static7.place(x=20, y=150)

#Static8 = tkinter.Label(text='Press(0) or Temp(1)')
#Static8.pack()
#Static8.place(x=30, y=20)

#Static9 = tkinter.Label(text='LP(0)/SP(1)')
#Static9.pack()
#Static9.place(x=30, y=40)

EditBox1 = tkinter.Entry(width=40)
EditBox1.insert(tkinter.END,"test.csv")
EditBox1.place(x=100, y=10)

EditBox2 = tkinter.Entry(width=20)
EditBox2.insert(tkinter.END,"0")
EditBox2.place(x=120, y=90)

EditBox3 = tkinter.Entry(width=20)
EditBox3.insert(tkinter.END,"0")
EditBox3.place(x=120, y=110)

EditBox4 = tkinter.Entry(width=20)
EditBox4.insert(tkinter.END,"0.00")
EditBox4.place(x=120, y=130)

EditBox5 = tkinter.Entry(width=20)
EditBox5.insert(tkinter.END,"26")
EditBox5.place(x=120, y=150)

#EditBox6 = tkinter.Entry(width=20)
#EditBox6.insert(tkinter.END,"0")
#EditBox6.place(x=150, y=20)

#EditBox7 = tkinter.Entry(width=20)
#EditBox7.insert(tkinter.END,"0")
#EditBox7.place(x=150, y=40)

Button1 = tkinter.Button(text='plot', width=15)
Button1.bind("<Button-1>",ButtonEvent)#左クリック（<Button-1>）されると，ButtonEvent関数を呼び出すようにバインド
Button1.place(x=270, y=95)

Button2 = tkinter.Button(text='exit',command=root.quit, width=15)
Button2.place(x=270, y=140)

root.mainloop()
