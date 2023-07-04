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

    pressN=14
    tempN=11

    tp = var1.get()
    SorL = var2.get()

    filepath = EditBox1.get()
    filepath = "caltable_data/"+filepath
    #print(filepath)
    Chc = EditBox2.get()
    Ch = int(Chc)
    #print(Chc)
    GasNumc = EditBox3.get()
    GasNum = int(GasNumc)
    if tp == 0:
        Tempc = EditBox4.get()
        Temp = float(Tempc)
    elif tp ==1:
        Pressc = EditBox5.get()
        Press = int(Pressc)

    data=[]

    if tp==0:
        for i1 in range(0,tempN):
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

                tempax=[-0.1,-0.08,-0.06,-0.04,-0.02,0,0.02,0.04,0.06,0.08,0.1]
                pressax=[18,20,22,24,26,28,30,32,34,36,38,40,42,44]
                featax=[1,2,3,4,5,6,7,8,9,10,11,12]
                x0 = pressax
                x1 = featax

                y0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y5 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y6 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y7 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y8 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y9 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y10 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y11 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

                y0_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y1_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y2_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y3_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y4_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y5_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y6_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y7_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y8_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y9_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y10_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y11_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y12_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y13_2 = [0,0,0,0,0,0,0,0,0,0,0]

                y0[i1] = data2[0]
                y1[i1] = data2[1]
                y2[i1] = data2[2]
                y3[i1] = data2[3]
                y4[i1] = data2[4]
                y5[i1] = data2[5]
                y6[i1] = data2[6]
                y7[i1] = data2[7]
                y8[i1] = data2[8]
                y9[i1] = data2[9]
                y10[i1] = data2[10]
                y11[i1] = data2[11]

                y0_2[i1] = data[0]
                y1_2[i1] = data[1]
                y2_2[i1] = data[2]
                y3_2[i1] = data[3]
                y4_2[i1] = data[4]
                y5_2[i1] = data[5]
                y6_2[i1] = data[6]
                y7_2[i1] = data[7]
                y8_2[i1] = data[8]
                y9_2[i1] = data[9]
                y10_2[i1] = data[10]
                y11_2[i1] = data[11]
                y12_2[i1] = data[12]
                y13_2[i1] = data[13]
        #print(y0)
        #sys.exit()

    elif tp==1:
        for i1 in range(0,pressN):
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

                tempax=[-0.1,-0.08,-0.06,-0.04,-0.02,0,0.02,0.04,0.06,0.08,0.1]
                pressax=[18,20,22,24,26,28,30,32,34,36,38,40,42,44]
                featax=[1,2,3,4,5,6,7,8,9,10,11,12]

                x1 = featax

                y0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y5 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y6 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y7 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y8 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y9 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y10 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                y11 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

                y0_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y1_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y2_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y3_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y4_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y5_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y6_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y7_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y8_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y9_2 = [0,0,0,0,0,0,0,0,0,0,0]
                y10_2 = [0,0,0,0,0,0,0,0,0,0,0]

                y0[i1] = data2[0]
                y1[i1] = data2[1]
                y2[i1] = data2[2]
                y3[i1] = data2[3]
                y4[i1] = data2[4]
                y5[i1] = data2[5]
                y6[i1] = data2[6]
                y7[i1] = data2[7]
                y8[i1] = data2[8]
                y9[i1] = data2[9]
                y10[i1] = data2[10]
                y11[i1] = data2[11]

                y0_2[i1] = data[0]
                y1_2[i1] = data[1]
                y2_2[i1] = data[2]
                y3_2[i1] = data[3]
                y4_2[i1] = data[4]
                y5_2[i1] = data[5]
                y6_2[i1] = data[6]
                y7_2[i1] = data[8]
                y8_2[i1] = data[7]
                y9_2[i1] = data[9]
                y10_2[i1] = data[10]

    fig = plt.figure(figsize=(15,15))
    ax1=[]
    ax2=[]
    if tp ==0:
        for i1 in range(0,tempN):
            ax1[i1] = fig.add_subplot(2, tempN, 2*i1)
            ax1[i1].plot(x0,y0[i1],x0,y1[i1],x0,y2[i1],x0,y3[i1],x0,y4[i1],x0,y5[i1],x0,y6[i1],x0,y7[i1],x0,y8[i1],x0,y9[i1],x0,y10[i1],x0,y11[i1])
            ax1[i1].set_xlabel("Pressure")
    elif tp == 1:
        for i1 in range(0,pressN):
            ax1[i1].set_xlabel("Temparature")
    else:
        pass
    if tp == 0:
        for i1 in range(0,tempN):
            ax1[i1].set_ylabel("arb.unit")
            ax1[i1].grid(which="both")
    else:
        for i1 in range(0,pressN):
            ax1[i1].set_ylabel("arb.unit")
            ax1[i1].grid(which="both")

    if tp == 0:
        ax2[i1] = fig.add_subplot(2, tempN, 2*i1+1)
    else:
        ax2[i1] = fig.add_subplot(2,pressN,2*i1+1)
    if tp == 0:
        for i1 in range(0,tempN):
            ax2[i1].plot(x1,y0_2[i1],x1,y1_2[i1],x1,y2_2[i1],x1,y3_2[i1],x1,y4_2[i1],x1,y5_2[i1],x1,y6_2[i1],x1,y7_2[i1],x1,y8_2[i1],x1,y9_2[i1],x1,y10_2[i1],x1,y11_2[i1],x1,y12_2[i1],x1,y13_2[i1])
    elif tp == 1:
        for i1 in range(0,pressN):
            ax2[i1].plot(x1,y0_2[i1],x1,y1_2[i1],x1,y2_2[i1],x1,y3_2[i1],x1,y4_2[i1],x1,y5_2[i1],x1,y6_2[i1],x1,y7_2[i1],x1,y8_2[i1],x1,y9_2[i1],x1,y10_2[i1])
    else:
        pass
    if tp == 0:
        for i1 in range(0,tempN):
            ax2[i1].set_xlabel("num")
            ax2[i1].set_xlim(0,13)
            ax2[i1].set_ylabel("arb.unit")
            ax2[i1].grid(which="both")
    else:
        for i1 in range(0,pressN):
            ax2[i1].set_xlabel("num")
            ax2[i1].set_xlim(0,13)
            ax2[i1].set_ylabel("arb.unit")
            ax2[i1].grid(which="both")
    #plt.savefig(a.png)
root = tkinter.Tk()
root.title("Calibration Table 16")
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
EditBox1.insert(tkinter.END,"test4.csv")
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
