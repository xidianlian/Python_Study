import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange

data =pd.read_csv('E:\\lian_workspace\\Files\\svm_test.csv')
x=data.ix[:,'x'].values
y=data.ix[:,'y'].values
label=data.ix[:,'label'].values

plt.figure(figsize=(8,6))
len=len(x)

for i in arange(len):
    if label[i]==1:
        plt.scatter(x[i],y[i],marker='*',c='r')
    else:
        plt.scatter(x[i],y[i],marker='.',c='b')
     
plt.show()
