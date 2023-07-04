import sys
import tkinter
import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def rownum_culc(a,b):
    return int((a+0.1)/0.02)*168+int((b-18)/2)*12
def colnum_culc(c,d,e):
    return c*20+d*5+e
def ButtonEvent(event):

    if Val_port.get() == True:
        tp=1
    else:
        tp=0

    if Val_lors.get() == True:
        SorL=1
    else:
        SorL=0

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
    filepath = EditBox_path.get()
    Chc = EditBox_ch.get()
    Ch = int(Chc)-1
    #print(Chc)
    GasNumc = EditBox_gas.get()
    GasNum = int(GasNumc)-1
    if tp == 0:
        Tempc = EditBox_temp.get()
        Temp = float(Tempc)
    elif tp ==1:
        Pressc = EditBox_press.get()
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
root.title("Calibration Table 13")
root.geometry("400x150")

# チェックボックスの各項目の初期値
Val_lors = tkinter.BooleanVar()
Val_port = tkinter.BooleanVar()

Val_lors.set(False)
Val_port.set(False)

Static_path = tkinter.Label(text="file path")
Static_path.pack()
Static_path.place(x=30, y=0)

CheckBox_port = tkinter.Checkbutton(text="Temp: check, Press: do not check", variable=Val_port)
CheckBox_port.place(x=100, y=20)

CheckBox_lors = tkinter.Checkbutton(text="SP: check, LP: do not check", variable=Val_lors)
CheckBox_lors.place(x=100, y=40)

Static_path = tkinter.Label(text='Ch # 1-4')
Static_path.pack()
Static_path.place(x=30, y=60)

Static_gas = tkinter.Label(text='Gas # (1-5)')
Static_gas.pack()
Static_gas.place(x=30, y=80)

Static_temp = tkinter.Label(text='Temp')
Static_temp.pack()
Static_temp.place(x=30, y=100)

Static_press = tkinter.Label(text='Press')
Static_press.pack()
Static_press.place(x=30, y=120)

#Static8 = tkinter.Label(text='Press(0) or Temp(1)')
#Static8.pack()
#Static8.place(x=30, y=20)

#Static9 = tkinter.Label(text='LP(0)/SP(1)')
#Static9.pack()
#Static9.place(x=30, y=40)

EditBox_path = tkinter.Entry(width=20)
EditBox_path.insert(tkinter.END,"test.csv")
EditBox_path.place(x=150, y=0)

EditBox_ch = tkinter.Entry(width=20)
EditBox_ch.insert(tkinter.END,"1")
EditBox_ch.place(x=150, y=60)

EditBox_gas = tkinter.Entry(width=20)
EditBox_gas.insert(tkinter.END,"1")
EditBox_gas.place(x=150, y=80)

EditBox_temp = tkinter.Entry(width=20)
EditBox_temp.insert(tkinter.END,"0.00")
EditBox_temp.place(x=150, y=100)

EditBox_press = tkinter.Entry(width=20)
EditBox_press.insert(tkinter.END,"26")
EditBox_press.place(x=150, y=120)

#EditBox6 = tkinter.Entry(width=20)
#EditBox6.insert(tkinter.END,"0")
#EditBox6.place(x=150, y=20)

#EditBox7 = tkinter.Entry(width=20)
#EditBox7.insert(tkinter.END,"0")
#EditBox7.place(x=150, y=40)

Button = tkinter.Button(text='plot')
Button.bind("<Button-1>",ButtonEvent)#左クリック（<Button-1>）されると，ButtonEvent関数を呼び出すようにバインド
Button.place(x=320, y=80)

root.mainloop()
