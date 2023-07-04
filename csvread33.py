import sys
import tkinter
import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def rownum_culc(a,b):
    return int((a+0.1)/0.02)*168+int((b-18)/2)*12
def colnum_culc(c,d,e):
    return c*20+d*5+e+10
def ButtonEvent(event):
    tpc = EditBox_PorT.get()
    tp = int(tpc)
    if tp == 0:
        EditBox_press.delete(0, tkinter.END)
    elif tp == 1:
        EditBox_temp.delete(0, tkinter.END)
    else:
        pass
    filepath = EditBox_filepath.get()
    SorLc = EditBox_LorS.get()
    SorL = int(SorLc)
    Chc = EditBox_gasnum.get()
    Ch = int(Chc)-1
    print(Chc)
    GasNumc = EditBox_intgasnum.get()
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

    if tp == 0:
        i0end = 14
    if tp == 1:
        i0end = 11
    else:
        pass
    fig = plt.figure(figsize=(10, 8))
    for i0 in range(0,i0end):

	    if tp==0:
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
	    if tp ==0:
	        ax1[i0].set_xlabel("Pressure")
	    elif tp == 1:
	        ax1[i0].set_xlabel("Temparature")
	    else:
	        pass
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
        #ax1[i0].set_xlim(-5,5)
	    #ax2[i0].set_xlim(0,13)
	    ax2[i0].set_ylabel("arb.unit")
	    ax2[i0].grid()
   #plt.savefig(a.png)
    plt.show()
    input()

root = tkinter.Tk()
root.title(u"Calibration Table")
root.geometry("400x200")

#Static1 = tkinter.Label(text=u'test1')
#Static1.pack()
#Static1.place(x=100, y=200)

#Static2 = tkinter.Label(text=u'test2')
#Static2.pack()
#Static2.place(x=100, y=300)

Static_filepath = tkinter.Label(text=u'file path')
Static_filepath.pack()
Static_filepath.place(x=30, y=0)

Static_Ch = tkinter.Label(text=u'Ch')
Static_Ch.pack()
Static_Ch.place(x=30, y=20)

Static_gasnum = tkinter.Label(text=u'Gass #')
Static_gasnum.pack()
Static_gasnum.place(x=30, y=40)

Static_temp = tkinter.Label(text=u'Temp')
Static_temp.pack()
Static_temp.place(x=30, y=60)

Static_press = tkinter.Label(text=u'Press')
Static_press.pack()
Static_press.place(x=30, y=80)

Static_PorT = tkinter.Label(text=u'Press(0) or Temp(1)')
Static_PorT.pack()
Static_PorT.place(x=30, y=100)

Static_LorS = tkinter.Label(text=u'LP(0)/SP(1)')
Static_LorS.pack()
Static_LorS.place(x=30, y=120)

EditBox_filepath = tkinter.Entry(width=20)
EditBox_filepath.insert(tkinter.END,"test.csv")
EditBox_filepath.place(x=150, y=0)

EditBox_gasnum = tkinter.Entry(width=20)
EditBox_gasnum.insert(tkinter.END,"1")
EditBox_gasnum.place(x=150, y=20)

EditBox_intgasnum = tkinter.Entry(width=20)
EditBox_intgasnum.insert(tkinter.END,"1")
EditBox_intgasnum.place(x=150, y=40)

EditBox_temp = tkinter.Entry(width=20)
EditBox_temp.insert(tkinter.END,"0.06")
EditBox_temp.place(x=150, y=60)

EditBox_press = tkinter.Entry(width=20)
EditBox_press.insert(tkinter.END,"24")
EditBox_press.place(x=150, y=80)

EditBox_PorT = tkinter.Entry(width=20)
EditBox_PorT.insert(tkinter.END,"0")
EditBox_PorT.place(x=150, y=100)

EditBox_LorS = tkinter.Entry(width=20)
EditBox_LorS.insert(tkinter.END,"0")
EditBox_LorS.place(x=150, y=120)

Button = tkinter.Button(text=u'plot')
Button.bind("<Button-1>",ButtonEvent)
#左クリック（<Button-1>）されると，ButtonEvent関数を呼び出すようにバインド
Button.place(x=320, y=80)

root.mainloop()
