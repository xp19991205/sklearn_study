import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Colormap  #用这里面的颜色进行绘图
from sklearn.svm import SVC
from sklearn.datasets import make_circles,make_blobs,make_classification,make_moons #月亮形，对半分等形状
n_samples = 100 #统一样本量
datasets = [
                make_moons(n_samples=n_samples,noise=0.2,random_state=0),
                make_circles(n_samples=n_samples,noise=0.2,factor=0.5,random_state=1),
                make_blobs(n_samples=n_samples,centers=2,random_state=5),
                make_classification(n_samples=n_samples,n_features=2,n_informative=2,n_redundant=0,random_state=5)
            ]
Kernel = ["linear","poly","rbf","sigmoid"]
for X,y in datasets:
    plt.figure(figsize=(5,4))
    plt.scatter(X[:,0],X[:,1],c=y,s=50,cmap="rainbow")

plt.show()

n_rows = len(datasets)
n_colmn = len(Kernel)+1 #第一列放原分布的图
fig,axes = plt.subplots(n_rows,n_colmn,figsize=(20,16) )

#开始子图循环
for index,(X,y) in enumerate(datasets):#第一层循环，取出索引和四个数据集数据
    ax = axes[index,0] #第一列子图画原始数据
    ax.scatter(X[:,0],X[:,1],c=y,s=50,cmap = plt.cm.Paired,edgecolors ="k")
    #edgecolors：每个点的边缘颜色
    ax.set_xticks([])
    ax.set_yticks([])
    if index == 0:
        ax.set_title("Input_data")  # 为第一个图放上数据
    for knernel_index,core in enumerate(Kernel):
        ax = axes[index,knernel_index+1] #在第2，3，4列绘制分类的图像
        if index == 0:
            ax.set_title(Kernel[knernel_index])
        ax.set_xticks([])
        ax.set_yticks([])
        clf = SVC(kernel=core,gamma=2).fit(X, y)  # 输入簇及对应的标号
        #绘制决策边界
        x_min,x_max = X[:,0].min()-0.5,X[:,0].max()+0.5
        y_min, y_max = X[:, 1].min() - 0.5, X[:,1].max() + 0.5
        XX,YY = np.mgrid[x_min:x_max:200j,y_min:y_max:200j]
        Z = clf.decision_function(np.c_[XX.ravel(),YY.ravel()]).reshape(XX.shape)
        ax.pcolormesh(XX,YY,Z>0,shading="auto",cmap=plt.cm.Paired)

        score = clf.score(X,y)
        print(score)
        ax.scatter(X[:,0],X[:,1],c=y,zorder = 10,cmap = plt.cm.Paired,edgecolors ="k")
        ax.contour(XX, YY, Z, colors="k", levels=[-1, 0, 1],
                   alpha=0.5, linestyles=["--", "-", "--"])
        #为每张图添加分数
        ax.text(0.95,0.06,('%2f' %score).lstrip('0'),size=6,bbox=dict(boxstyle ="round",alpha =0.8,facecolor = "white")
                                                                       ,transform =ax.transAxes,horizontalalignment = 'right' )
        #bbox：添加格子 transAxes:确定坐标轴为子图的本身 horizontalalignment：位于坐标轴的方向
    print("index ={}".format(index))

plt.show()

#一般来说：先拿rbf来试试，poly多用于图像处理（也可以使用其他核函数）