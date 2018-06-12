import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange
rate = pd.read_csv('E:\\lian_workspace\\Files\\unrate.csv') 

rate=rate[0:12].T
position=arange(12)+1 #x坐标
#取出第一列数据，即'unrate'的值
height=rate.ix[1,:].values
fig,ax=plt.subplots()
ax.bar(position,height,0.3)#ax.barh（）横着显示
cols=rate.ix[0,:].values

ax.set_xticks(position)
ax.set_xticklabels(cols,rotation=25)#设置列的名称和选中角度
ax.set_xlabel('date')
ax.set_ylabel('values')
ax.set_title('Unrate')
plt.show()

