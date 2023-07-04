import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def rownum_culc(a,b):
    return int((a+0.1)/0.02)*168+int((b-18)/2)*12
def colnum_culc(c,d,e):
    return c*20+d*5+e

filepath=input("csv file path :")
#filepath="test3.csv"
tp=int(input("Pressure(0) or Temparature(1)? :"))
SorL = int(input("long (0) or short (1) :"))
Ch = int(input("NO:0, NO2:1, N2O:2, NH3:3 :"))
GasNum = int(input("main gas:0, interference gas:1,2,3,4 :"))
if tp == 0:
    Temp = float(input("from -0.1, to 0.1, 0.02 step :"))
elif tp == 1:
    Press = float(input("from 18 to 44, 2 step :"))
else:
    pass
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

fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(x0,y0,x0,y1,x0,y2,x0,y3,x0,y4,x0,y5,x0,y6,x0,y7,x0,y8,x0,y9,x0,y10,x0,y11)
if tp ==0:
    ax1.set_xlabel("Pressure")
elif tp == 1:
    ax1.set_xlabel("Temparature")
else:
    pass
ax1.set_ylabel("arb.unit")
ax1.grid()
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
ax2.grid()
#plt.savefig(a.png)
plt.show()
input()
