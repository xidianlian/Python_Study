import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rate=pd.read_csv("E:\\lian_workspace\\Files\\unrate.csv")
rate['DATE']=pd.to_datetime(rate['DATE'])
#子图
#fig=plt.figure();
fig=plt.figure(figsize=(6,6))#图的长宽
ax1 = fig.add_subplot(3,1,1)#子图以2行1列的形式排列，此为第一个图
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)
data1=rate[0:5]
data2=rate[6:10]
data3=rate[11:15]
ax1.plot(data1['DATE'],data1['UNRATE'])
ax2.plot(data2['DATE'],data2['UNRATE'])
ax3.plot(data2['DATE'],data2['UNRATE'],c='red',label='data2')#添加标注
ax3.plot(data3['DATE'],data3['UNRATE'],c='blue',label='data3')
ax3.legend(loc='upper left')#标注显示在哪里
#print(help(ax3.legend))
plt.show()