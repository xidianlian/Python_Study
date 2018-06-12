import pandas as pd
from numpy import *
from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt

##设置子图数量
fig, axes = plt.subplots(nrows=2, ncols=2,figsize=(7,7))
ax0, ax1, ax2, ax3 = axes.flatten()

#准备训练样本
def loadDataSet(filename): #读取数据
    dataMat=[]
    labelMat=[]
    df=pd.read_csv(filename)
    dataMat=df[["x","y"]]
    labelMat=df['label']
    return dataMat,labelMat #返回数据特征和数据类别
#准备训练样本
traindata='E:\\lian_workspace\\Files\\svm_train.csv'
testdata='E:\\lian_workspace\\Files\\svm_test.csv'
x,y=loadDataSet(traindata)
x=np.array(x).tolist()
y=np.array(y).tolist()

test_x,test_y=loadDataSet(testdata)
test_x=np.array(test_x).tolist()
test_y=np.array(test_y).tolist()
'''
    说明1：
       核函数(这里简单介绍了sklearn中svm的四个核函数，还有precomputed及自定义的)
        
    LinearSVC：主要用于线性可分的情形。参数少，速度快，对于一般数据，分类效果已经很理想
    RBF:主要用于线性不可分的情形。参数多，分类结果非常依赖于参数
    polynomial:多项式函数,degree 表示多项式的程度-----支持非线性分类
    Sigmoid：在生物学中常见的S型的函数，也称为S型生长曲线

    说明2：根据设置的参数不同，得出的分类结果及显示结果也会不同
    
'''
##设置子图的标题
titles = ['LinearSVC (linear kernel)',  
          'SVC with polynomial (degree 3) kernel',  
          'SVC with RBF kernel',      ##这个是默认的
          'SVC with Sigmoid kernel']
##生成随机试验数据(15行2列)
# rdm_arr=np.random.randint(1, 15, size=(15,2))

def drawPoint(ax,clf,tn):
    for i in x:
        ax.set_title(titles[tn])
        res=clf.predict(np.array(i).reshape(1, -1))
        if res > 0:
           ax.scatter(i[0],i[1],c='r',marker='*')
        else :
           ax.scatter(i[0],i[1],c='g',marker='*')
#     k=0
#     cnt=0;
#     m,n=shape(test_x)
#     for i in test_x:
#         res=clf.predict(np.array(i).reshape(1, -1))
#         if(res==test_y[k]):
#             cnt+=1
#         print("k:%d (%f,%f),res:%d  zheng:%d"%(k,i[0],i[1],res,test_y[k]))
#         k+=1
#         if res==1:
#            ax.scatter(i[0],i[1],c='r',marker='.')
#         else :
#            ax.scatter(i[0],i[1],c='g',marker='.')
#     print("Jingdu:%d  %f"%(cnt,float(cnt)/m))
if __name__=="__main__":
    ##选择核函数
    for n in range(0,4):
        if n==0:
            clf = svm.SVC(kernel='rbf').fit(x, y)
            drawPoint(ax2,clf,2)
#         elif n==1:
#             clf = svm.SVC(kernel='poly', degree=3).fit(x, y)
#             drawPoint(ax1,clf,1)
#         elif n==2:
#             clf= svm.SVC(kernel='rbf').fit(x, y)
#             drawPoint(ax2,clf,2)
#         else :
#             clf= svm.SVC(kernel='sigmoid').fit(x, y)
#             drawPoint(ax3,clf,3)
    plt.show()