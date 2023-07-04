import sys
import tkinter
import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def rownum_culc(a,b):
    return int((a+0.1)/0.02)*168+int((b-18)/2)*12+10
def colnum_culc(c,d,e):
    return c*20+d*5+e
def ButtonEvent(event):

    filepath = EditBox1.get()
    #filepath = "caltable_data\+filepath

    print(filepath)
    #sys.exit()

    tp = var1.get()
    SorL = var2.get()
    filepath = EditBox1.get()
    Chc = EditBox2.get()
    Ch = int(Chc)-1
    #print(Chc)
    GasNumc = EditBox3.get()
    GasNum = int(GasNumc)-1
    if tp == 0:
        Tempc = EditBox4.get()
        Temp = float(Tempc)
    elif tp ==1:
        Pressc = EditBox5.get()
        Press = int(Pressc)

    data=[]

    if tp == 0:
        i0end = 14
    if tp == 1:
        i0end = 11
    else:
        pass
    fig = plt.figure(figsize=(15, 8))

    for i0 in range(0,3):

	    if tp==0:
	        data=[]
	        for i in range(0,14):
	            Press=2*i+18
	            RowNum=rownum_culc(Temp,Press)
	            ColNum=colnum_culc(SorL,Ch,GasNum)
	            csvdata = pd.read_csv(filepath, header=None)
	            databf=csvdata.values[RowNum:RowNum+12,ColNum]
	            data.append(databf)
	            i=i+1

	        data2=[[0] * 14 for i in range(12)]
	        for i in range(12):
	            for j in range(14):
	                data2[i][j]=data[j][i]
	        #print(data)

	    elif tp==1:
	        data=[]
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

	    ax1=[0 for i1 in range(0,i0end)]
	    ax2=[0 for i1 in range(0,i0end)]
	    ax1[i0] = fig.add_subplot(2, i0end, i0+1)
	    ax1[i0].plot(x0,y0,x0,y1,x0,y2,x0,y3,x0,y4,x0,y5,x0,y6,x0,y7,x0,y8,x0,y9,x0,y10,x0,y11)
	    #if tp ==0:
	    #    ax1[i0].set_xlabel("Pressure")
	    #elif tp == 1:
	    #    ax1[i0].set_xlabel("Temparature")
	    #else:
	    #    pass
	    ax1[i0].set_ylabel("arb.unit")
	    ax1[i0].grid()
	    ax2[i0] = fig.add_subplot(2, i0end, i0+1+i0end)
	    if tp == 0:
	        ax2[i0].plot(x1,y0_2,x1,y1_2,x1,y2_2,x1,y3_2,x1,y4_2,x1,y5_2,x1,y6_2,x1,y7_2,x1,y8_2,x1,y9_2,x1,y10_2,x1,y11_2,x1,y12_2,x1,y13_2)
	    elif tp == 1:
	        ax2[i0].plot(x1,y0_2,x1,y1_2,x1,y2_2,x1,y3_2,x1,y4_2,x1,y5_2,x1,y6_2,x1,y7_2,x1,y8_2,x1,y9_2,x1,y10_2)
	    else:
	        pass
	    ax2[i0].set_xlabel("num")
	    #ax2[i0].set_xlim(0,13)
	    ax2[i0].set_ylabel("arb.unit")
	    ax2[i0].grid()
   #plt.savefig(a.png)
    plt.show()
    #input()
root = tkinter.Tk()
root.title("Calibration Table")
root.geometry("400x220")

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

Button1 = tkinter.Button(text='plot', width=15)
Button1.bind("<Button-1>",ButtonEvent)#左クリック（<Button-1>）されると，ButtonEvent関数を呼び出すようにバインド
Button1.place(x=270, y=95)

Button2 = tkinter.Button(text='exit',command=root.quit, width=15)
Button2.place(x=270, y=140)

root.mainloop()
