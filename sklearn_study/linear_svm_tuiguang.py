#简单案例解释核函数解决线性不可分问题
from sklearn.datasets import make_circles #用于制造线性不可分数据
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np
X,y = make_circles(n_samples=100,factor=0.1,noise=0.1) #factor内外圆半径的比值
plt.scatter(X[:,0],X[:,1],c = y,s=50,cmap="rainbow")
ax = plt.gca()#获取当前的图进行继续操作
#尝试使用原来定义的线性判别函数进行绘图
def plot_svc_decision_function(model,ax = None):
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
    Z = model.decision_function(xy).reshape(axisx.shape)  # 等于0，超平面，小于-1一类，大于1一类
    # 画决策边界和平行于决策边界的超平面
    ax.contour(axisx, axisy, Z, colors="k", levels=[-1, 0, 1],
               alpha=0.5, linestyles=["--", "-", "--"])
    ax.set_ylim(ylim)
    ax.set_xlim(xlim)
clf = SVC(kernel="linear").fit(X,y) #输入簇及对应的标号
plot_svc_decision_function(clf,ax)
plt.show()
print("分类准确度{}".format(clf.score(X,y)))


#为非线性数据增加维度并绘制图像
r = np.exp(-X**2).sum(1) #exp(-x1^2)+exp(-x2^2)
rlim = np.linspace(min(r),max(r),100)
from mpl_toolkits.mplot3d import Axes3D
def plot_3D(elev=30,azim=30,X=X,y=y) :
#elev:上下旋转的角度
#azim:左右旋转的角度
    ax = plt.subplot(projection = '3d')
    ax.scatter3D(X[:,0],X[:,1],r,c=y,s=50,cmap="rainbow")
    ax.view_init(elev,azim)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('r')
    plt.show()

# plot_3D()
from ipywidgets import interact,fixed
interact(plot_3D,elev=[0,30,60,90,120],azim = (-180.180),X=fixed(X),y=fixed(y))
plt.show()

#在二维不能解决的，我们可以加上一个维度（核变换） 寻找线性可分的超平面
clf = SVC(kernel="rbf").fit(X,y) #输入簇及对应的标号
plt.scatter(X[:,0],X[:,1],c = y,s=50,cmap="rainbow")
ax = plt.gca()
plot_svc_decision_function(clf,ax)
plt.show()
#这里与前面r的处理方式类似，称作高斯径向基rbf
#其他可以使用的和函数有linear/poly(多项式核/偏线性)
#“sigmoid”双曲正切核：解决非线性问题


clf = SVC(kernel="poly").fit(X,y) #输入簇及对应的标号
plt.scatter(X[:,0],X[:,1],c = y,s=50,cmap="rainbow")
ax = plt.gca()
plot_svc_decision_function(clf,ax)
plt.show()
print("poly核函数准确度为{}".format(clf.score(X,y)))

clf = SVC(kernel="sigmoid").fit(X,y) #输入簇及对应的标号
plt.scatter(X[:,0],X[:,1],c = y,s=50,cmap="rainbow")
ax = plt.gca()
plot_svc_decision_function(clf,ax)
plt.show()
print("sigmoid核函数准确度为{}".format(clf.score(X,y)))

clf = SVC(kernel="rbf").fit(X,y) #输入簇及对应的标号
plt.scatter(X[:,0],X[:,1],c = y,s=50,cmap="rainbow")
ax = plt.gca()
plot_svc_decision_function(clf,ax)
plt.show()
print("rbf核函数准确度为{}".format(clf.score(X,y)))