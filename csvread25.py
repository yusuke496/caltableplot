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

    #SorL = 0
    #Ch = 0
    #GasNum = 0
    #Temp = 0
    #Press = 18
    indicator=str(0)
    tempN=11
    pressN=14
    i=0
    j=0
    data=[]
    data_last=[]
    if tp==0:
        #data = [[0, 0], [0 for i in range(12)]]
        #data = [[0 for in range(tempN)],[0 for in range(12)]]
        for j in range(0,tempN):
            Temp=0.02*j-0.1
            for i in range(0,pressN):
                Press=2*i+18
                indicator=j
                RowNum=rownum_culc(Temp,Press)
                ColNum=colnum_culc(SorL,Ch,GasNum)
                csvdata = pd.read_csv(filepath, header=None)
                databf=csvdata.values[RowNum:RowNum+12,ColNum]
                data.append(databf)
                data[j][:]=databf
                #data=np.array(data)
                i=i+1
            j=j+1
        data=np.array(data)
        for i in range(0,tempN):
            data[i]=data[i].T
            i=i+1
        data_final=[]
        for i in range(0,tempN):
            data_final[i,:]=data[i,tempN]
            i=i+1
        print(data)
        sys.exit()
        #print(dataname)
        #sys.exit()

    elif tp==1:
        data = [[0, 0], [0 for i in range(12)]]
        #data = [[0 for in range(pressN)],[0 for in range(12)]]
        for j in range(0,pressN):
            Press=2*j+18
            for i in range(0,tempN):
                Temp=0.02*i-0.1
                indicator=j
                RowNum=rownum_culc(Temp,Press)
                ColNum=colnum_culc(SorL,Ch,GasNum)
                csvdata = pd.read_csv(filepath, header=None)
                databf=csvdata.values[RowNum:RowNum+12,ColNum]
                data.append(databf)
                data[j][:]=databf
                #data=np.array(data)
                i=i+1
            j=j+1
        data=np.array(data)
        for i in range(0,pressN):
            data[i]=data[i].T
            i=i+1
        for i in range(0,pressN):
            data_final[i,:]=data[i,pressN]
            i=i+1
        print(data)
        sys.exit()


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

    y1_0 = data[0][0]
    y1_1 = data[0][1]
    y1_2 = data[0][2]
    y1_3 = data[0][3]
    y1_4 = data[0][4]
    y1_5 = data[0][5]
    y1_6 = data[0][6]
    y1_7 = data[0][7]
    y1_8 = data[0][8]
    y1_9 = data[0][9]
    y1_10 = data[0][10]


    y2_0 = data[1][0]
    y2_1 = data[1][1]
    y2_2 = data[1][2]
    y2_3 = data[1][3]
    y2_4 = data[1][4]
    y2_5 = data[1][5]
    y2_6 = data[1][6]
    y2_7 = data[1][7]
    y2_8 = data[1][8]
    y2_9 = data[1][9]
    y2_10 = data[1][10]


    if tp == 0:
        y1_11 = data[0][11]
        y1_12 = data[0][12]
        y1_13 = data[0][13]
        y2_11 = data[1][11]
        y2_12 = data[1][12]
        y2_13 = data[1][13]
    elif tp == 1:
        pass
    else:
        pass

    fig = plt.figure(figsize=(12, 4))
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax1.plot(x0,y1_0,x0,y1_1,x0,y1_2,x0,y1_3,x0,y1_4,x0,y1_5,x0,y1_6,x0,y1_7,x0,y1_8,x0,y1_9,x0,y1_10,x0,y1_11,y1_12,y1_13)
    ax2.plot(x0,y2_0,x0,y2_1,x0,y2_2,x0,y2_3,x0,y2_4,x0,y2_5,x0,y2_6,x0,y2_7,x0,y2_8,x0,y2_9,x0,y2_10,x0,y2_11,y2_12,y2_13)
    if tp ==0:
        ax1.set_xlabel("Pressure")
        ax2.set_xlabel("Pressure")
    elif tp == 1:
        ax1.set_xlabel("Temparature")
        ax2.set_xlabel("Tempareture")
    else:
        pass
    ax1.set_ylabel("arb.unit")
    ax1.grid(which="both")
    ax2 = fig.add_subplot(2, 1, 2)
    if tp == 0:
        ax1.plot(x0,y1_0,x0,y1_1,x0,y1_2,x0,y1_3,x0,y1_4,x0,y1_5,x0,y1_6,x0,y1_7,x0,y1_8,x0,y1_9,x0,y1_10,x0,y1_11)
        ax2.plot(x0,y2_0,x0,y2_1,x0,y2_2,x0,y2_3,x0,y2_4,x0,y2_5,x0,y2_6,x0,y2_7,x0,y2_8,x0,y2_9,x0,y2_10,x0,y2_11)
    elif tp == 1:
        ax1.plot(x0,y1_0,x0,y1_1,x0,y1_2,x0,y1_3,x0,y1_4,x0,y1_5,x0,y1_6,x0,y1_7,x0,y1_8,x0,y1_9,x0,y1_10,x0,y1_11)
        ax2.plot(x0,y2_0,x0,y2_1,x0,y2_2,x0,y2_3,x0,y2_4,x0,y2_5,x0,y2_6,x0,y2_7,x0,y2_8,x0,y2_9,x0,y2_10,x0,y2_11)
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
root.title("Calibration Table")
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
