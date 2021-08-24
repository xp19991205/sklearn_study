#这个程序主要是用来考虑svc中的c参数对模型的影响，就是控制软间隔的程度，越大，越接近硬间隔
from sklearn.datasets import load_breast_cancer #导入乳腺癌数据，总共500多条，30多个特征
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from time import time #计时模块
import datetime #把时间戳转化为真实时间
#加载数据
data = load_breast_cancer()
X = data.data #569*30
y = data.target #569
#标准化数据
from sklearn.preprocessing import StandardScaler
# X = StandardScaler().fit_transform(X)
#划分训练集，测试集
X_train,X_test,Y_train,Y_test = train_test_split(X,y,test_size=0.3,random_state=420)
#
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
#
c_range = np.linspace(0.01,30,50)
score = []
for r in c_range:
    clf = SVC(kernel="linear",C=r,cache_size=5000).fit(X_train,Y_train) #注意是C不是c
    score.append(clf.score(X_test,Y_test))

plt.plot(c_range,score)
plt.show()
print(max(score),c_range[score.index(max(score))])

#换rbf
score = []
for r in c_range:
    clf = SVC(kernel="rbf",C=r,gamma=0.010722672220103254,cache_size=5000).fit(X_train,Y_train) #注意是C不是c
    score.append(clf.score(X_test,Y_test))
#前面的gamma是kernel_parameters.py中一维搜索找到的 在这个基础上通过优化c（软间隔参数）进一步优化了SVM的分类效果
plt.plot(c_range,score)
plt.show()
print(max(score),c_range[score.index(max(score))])