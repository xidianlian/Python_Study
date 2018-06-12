import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy.physics.quantum.spin import Rotation

rate=pd.read_csv("E:\\lian_workspace\\Files\\UNRATE.csv")
rate['DATE']=pd.to_datetime(rate['DATE'])
#print(rate.head(1))
first_twelve=rate[0:11]
plt.plot(first_twelve['DATE'],first_twelve['UNRATE'])
#设置横坐标旋转角度
plt.xticks(rotation=20)
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Trends in 1948')
plt.show()

