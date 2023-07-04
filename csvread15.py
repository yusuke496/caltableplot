import sys
import tkinter
import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def rownum_culc(a,b):
    return int((a+0.1)/0.02)*168+int((b-18)/2)*12+8
def colnum_culc(c,d,e):
    return c*20+d*5+e
def ButtonEvent(event):
    #if Val1.get() == True:
    #    tp=1
    #else:
    #    tp=0

    #if Val2.get() == True:
    #    SorL=1
    #else:
    #    SorL=0

    tp = var1.get()
    SorL = var2.get()

    #tpc = EditBox6.get()
    #tp = int(tpc)
    #SorLc = EditBox7.get()
    #SorL = int(SorLc)
#    if tp == 0:
#        EditBox5.delete(0, tkinter.END)
#    elif tp == 1:
#        EditBox4.delete(0, tkinter.END)
#    else:
#        pass
    filepath = EditBox1.get()
    filepath = "data/"+filepath
    #print(filepath)
    Chc = EditBox2.get()
    Ch = int(Chc)
    Ch = Ch - 1
    #print(Chc)
    GasNumc = EditBox3.get()
    GasNum = int(GasNumc)
    GasNum = GasNum - 1
    if tp == 0:
        Tempc = EditBox4.get()
        Temp = float(Tempc)
    elif tp ==1:
        Pressc = EditBox5.get()
        Press = int(Pressc)

    #SorL = 0
    #Ch = 0
    #GasNum = 0
    #Temp = 0
    #Press = 18

    data=[]

    if tp==0:
        for i in range(0,14):
            Press=2*i+18
            RowNum=rownum_culc(Temp,Press)
            ColNum=colnum_culc(SorL,Ch,GasNum)
            csvdata = pd.read_csv(filepath, header=None)
            databf=csvdata.values[RowNum:RowNum+12,ColNum]
            #print(databf[0])
            data.append(databf)
            i=i+1

        data2=[[0] * 14 for i in range(12)]
        for i in range(12):
            for j in range(14):
                data2[i][j]=data[j][i]
        #print(data)

    elif tp==1:
        for i in range(0,11):
            Temp=0.02*i-0.1
            #print(Temp)
            RowNum=rownum_culc(Temp,Press)
            ColNum=colnum_culc(SorL,Ch,GasNum)
            csvdata = pd.read_csv(filepath, header=None)
            databf=csvdata.values[RowNum:RowNum+12,ColNum]
            data.append(databf)
            i=i+1

        data2=[[0] * 11 for i in range(12)]
        for i in range(12):
            for j in range(11):
                data2[i][j]=data[j][i]
        #print(data)

    else:
        pass


    tempax=[-0.1,-0.08,-0.06,-0.04,-0.02,0,0.02,0.04,0.06,0.08,0.1]
    pressax=[18,20,22,24,26,28,30,32,34,36,38,40,42,44]
    featax=[1,2,3,4,5,6,7,8,9,10,11,12]

    if tp == 0:
        x0 = pressax
    elif tp == 1:
        x0 = tempax
    else:
        pass

    x1 = featax

    y0 = data2[0]
    y1 = data2[1]
    y2 = data2[2]
    y3 = data2[3]
    y4 = data2[4]
    y5 = data2[5]
    y6 = data2[6]
    y7 = data2[7]
    y8 = data2[8]
    y9 = data2[9]
    y10 = data2[10]
    y11 = data2[11]

    y0_2 = data[0]
    y1_2 = data[1]
    y2_2 = data[2]
    y3_2 = data[3]
    y4_2 = data[4]
    y5_2 = data[5]
    y6_2 = data[6]
    y7_2 = data[7]
    y8_2 = data[8]
    y9_2 = data[9]
    y10_2 = data[10]

    if tp == 0:
        y11_2 = data[11]
        y12_2 = data[12]
        y13_2 = data[13]
    elif tp == 1:
        pass
    else:
        pass

    fig = plt.figure(figsize=(6, 4))
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(x0,y0,x0,y1,x0,y2,x0,y3,x0,y4,x0,y5,x0,y6,x0,y7,x0,y8,x0,y9,x0,y10,x0,y11)
    if tp ==0:
        ax1.set_xlabel("Pressure")
    elif tp == 1:
        ax1.set_xlabel("Temparature")
    else:
        pass
    ax1.set_ylabel("arb.unit")
    ax1.grid(which="both")
    ax2 = fig.add_subplot(2, 1, 2)
    if tp == 0:
        ax2.plot(x1,y0_2,x1,y1_2,x1,y2_2,x1,y3_2,x1,y4_2,x1,y5_2,x1,y6_2,x1,y7_2,x1,y8_2,x1,y9_2,x1,y10_2,x1,y11_2,x1,y12_2,x1,y13_2)
    elif tp == 1:
        ax2.plot(x1,y0_2,x1,y1_2,x1,y2_2,x1,y3_2,x1,y4_2,x1,y5_2,x1,y6_2,x1,y7_2,x1,y8_2,x1,y9_2,x1,y10_2)
    else:
        pass
    ax2.set_xlabel("num")
    ax2.set_xlim(0,13)
    ax2.set_ylabel("arb.unit")
    ax2.grid(which="both")
    #plt.savefig(a.png)
    fig.show()
    #input()

root = tkinter.Tk()
root.title("Calibration Table 15")
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

Static3 = tkinter.Label(text='file name')
Static3.pack()
Static3.place(x=20, y=10)

Static4 = tkinter.Label(text='Ch (1~4)')
Static4.pack()
Static4.place(x=20, y=90)

Static5 = tkinter.Label(text='Gass # (1~5)')
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
EditBox2.insert(tkinter.END,"1")
EditBox2.place(x=120, y=90)

EditBox3 = tkinter.Entry(width=20)
EditBox3.insert(tkinter.END,"1")
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
