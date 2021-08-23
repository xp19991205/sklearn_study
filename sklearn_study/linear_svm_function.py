#这里是把前面的画图打包成一个具体的函数
#第一步：导入本程序所有需要的包
from sklearn.datasets import make_blobs
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

def plot_linear_svc_decision_function(model,ax = None):
    if ax ==None:
        ax = plt.gca()#创建新的子图
    ylim = ax.get_ylim()
    xlim = ax.get_xlim()
    axis_x = np.linspace(xlim[0], xlim[1], 30)  # 在最大最小的坐标上产生取30个点
    axis_y = np.linspace(ylim[0], ylim[1], 30)
    axisx, axisy = np.meshgrid(axis_x, axis_y)
    # axisx:30*30 axisy:30*30
    # axis_x 对应一直循环最小到最大（取样） 30点一循环
    xy = np.vstack([axisx.ravel(), axisy.ravel()]).T  # 主要功能是把二维数据转为一维
    # ravel主要是把多维数组转化为一维数组 30*30 =900
    # np.stack这个函数主要是把以一维化的x和y拼成(x,y)的对应形式（垂直按行顺序拼接）
    # 注意x，y都是按行摆的，那么一拼接就是2*900 转置一下就得到了900个平面上的点

    # 建模：通过fit计算得出对应的决策边界
    model = SVC(kernel="linear").fit(X, y)  # 输入簇及对应的标号
    Z = model.decision_function(xy).reshape(axisx.shape)  # 等于0，超平面，小于-1一类，大于1一类
    # 画决策边界和平行于决策边界的超平面
    ax.contour(axisx, axisy, Z, colors="k", levels=[-1, 0, 1],
               alpha=0.5, linestyles=["--", "-", "--"])
    ax.set_ylim(ylim)
    ax.set_xlim(xlim)



#第二步：准备相应的需要分类的数据和标签
X,y = make_blobs(n_samples=50,centers=2,random_state=0,cluster_std=0.6)#初始化生成簇
print(y.shape)
#注意X[:][0]的写法只取得出来一行，是错误的写法
#cmap:就是colormap
clf = SVC(kernel="linear").fit(X,y) #输入簇及对应的标号
plt.scatter(X[:,0],X[:,1],c=y,s=50,cmap="rainbow") #参数c就是color，赋值为可迭代参数对象,s代表size指代点的大小（要么统一要么指定所有点的大小）
plt.xticks([])
plt.yticks([]) #不要显示坐标
#第三步：绘制决策边界(采用等高线countour)
ax = plt.gca()#获取当前的图进行继续操作


#建模：通过fit计算得出对应的决策边界

plot_linear_svc_decision_function(clf,ax)
plt.show()

#下面对相应的线性svm的相关功能做介绍
print(clf.predict(X)) #根据决策边界做相应的预测
print(clf.predict([[3,3]])) #根据决策边界做相应的预测
print(clf.score(X,y)) #计算分类的准确度（可以用于测试集）
print(clf.support_vectors_)#三个支持向量对应的坐标(距离超平面最近的且满足一定条件的几个训练样本点)
print(clf.n_support_) #第一类中有2个支持向量，第二类中有1个支持向量