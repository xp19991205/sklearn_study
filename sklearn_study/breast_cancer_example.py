#导入模块
from sklearn.datasets import load_breast_cancer #导入乳腺癌数据，总共500多条，30多个特征
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from time import time #计时模块
import datetime #把时间戳转化为真实时间
#实例化数据
data = load_breast_cancer()
X = data.data #569*30
y = data.target #569
#首先利用PCA降维试试
from sklearn.decomposition import PCA
pca = PCA(n_components=2).fit(X)
X_dr = pca.transform(X)
#然后绘图
plt.scatter(X_dr[:,0],X_dr[:,1],s=15,c=y,cmap="rainbow")
plt.show()
#主成分分析得到的结果仍然是交织在一起的

#划分训练集，测试集
X_train,X_test,Y_train,Y_test = train_test_split(X,y,test_size=0.3,random_state=420)
# Kernel = ["linear","rbf","sigmoid"]
# for kernel in Kernel:
#     time0 = time()
#     clf = SVC(kernel= kernel,gamma="auto",cache_size=5000).fit(X_train,Y_train) #默认200MB
#     #cache:代表允许SVM使用的内存大小，这与电脑配置有关，默认是200（MB）
#     print("The accuracy under kernel %s is %f" %(kernel,clf.score(X_text,Y_test)))
#     print(datetime.datetime.fromtimestamp(time()-time0).strftime("%M:%S:%f"))
#第一次卡在了多项式函数，因为degree =3让python内核崩溃
# now = time() #获取时间戳timestamp
# print(datetime.datetime.fromtimestamp(now).strftime("%Y-%m-%d,%H:%M:%S:%f"))

Kernel = ["linear","poly","rbf","sigmoid"]
for kernel in Kernel:
    time0 = time()
    clf = SVC(kernel= kernel,gamma="auto",cache_size=5000,degree = 2).fit(X_train,Y_train) #默认200MB
    #cache:代表允许SVM使用的内存大小，这与电脑配置有关，默认是200（MB）
    print("The accuracy under kernel %s is %f" %(kernel,clf.score(X_test,Y_test)))
    print(datetime.datetime.fromtimestamp(time()-time0).strftime("%M:%S:%f"))
#degree = 2比1 时间多花很多，准确度从92到了94
import pandas as pd
data = pd.DataFrame(X)
describe = pd.DataFrame(data.describe([0.01,0.05,0.1,0.25,0.5,0.75,0.99]))
describe.to_excel('./describe.xlsx')
#查看均值可以看到明显的量纲不统一，不是正态分布（偏态）,下面选择标准化
from sklearn.preprocessing import StandardScaler
X = StandardScaler().fit_transform(X)
data_atfer_preprocess = pd.DataFrame(X)
data_atfer_preprocess.to_excel('./data_atfer_preprocess.xlsx')
describe_after_process = pd.DataFrame(data_atfer_preprocess.describe([0.01,0.05,0.1,0.25,0.5,0.75,0.99]))
describe_after_process.to_excel('./describe_afterprocess.xlsx')
#用处理完的数据继续跑前面的代码
X_train,X_test,Y_train,Y_test = train_test_split(X,y,test_size=0.3,random_state=420)
Kernel = ["linear","poly","rbf","sigmoid"]
for kernel in Kernel:
    time0 = time()
    clf = SVC(kernel= kernel,gamma="auto",cache_size=5000,degree = 1).fit(X_train,Y_train) #默认200MB
    #cache:代表允许SVM使用的内存大小，这与电脑配置有关，默认是200（MB）
    print("The accuracy under kernel %s is %f" %(kernel,clf.score(X_test,Y_test)))
    print(datetime.datetime.fromtimestamp(time()-time0).strftime("%M:%S:%f"))

#通过这个案例：得出以下结论:
#1.线性核尤其是多项式核在高次项时计算缓慢
#2.rbf和多项式核函数都不擅长处理量纲不统一的数据