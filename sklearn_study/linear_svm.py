#第一步：导入本程序所有需要的包
from sklearn.datasets import make_blobs
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np
#第二步：准备相应的需要分类的数据和标签
X,y = make_blobs(n_samples=50,centers=2,random_state=0,cluster_std=0.6)#初始化生成簇
print(y.shape)
#注意X[:][0]的写法只取得出来一行，是错误的写法
#cmap:就是colormap
plt.scatter(X[:,0],X[:,1],c=y,s=50,cmap="rainbow") #参数c就是color，赋值为可迭代参数对象,s代表size指代点的大小（要么统一要么指定所有点的大小）
plt.xticks([])
plt.yticks([]) #不要显示坐标
#第三步：绘制决策边界(采用等高线countour)
ax = plt.gca()#获取当前的图进行继续操作
#首先我们来制作网格meshgird
ylim = ax.get_ylim()
xlim = ax.get_xlim()
axis_x = np.linspace(xlim[0],xlim[1],30)#在最大最小的坐标上产生取30个点
axis_y = np.linspace(ylim[0],ylim[1],30)
axisx,axisy = np.meshgrid(axis_x,axis_y)
#axisx:30*30 axisy:30*30
#axis_x 对应一直循环最小到最大（取样） 30点一循环
xy = np.vstack([axisx.ravel(),axisy.ravel()]).T #主要功能是把二维数据转为一维
#ravel主要是把多维数组转化为一维数组 30*30 =900
#np.stack这个函数主要是把以一维化的x和y拼成(x,y)的对应形式（垂直按行顺序拼接）
#注意x，y都是按行摆的，那么一拼接就是2*900 转置一下就得到了900个平面上的点

#建模：通过fit计算得出对应的决策边界
clf = SVC(kernel="linear").fit(X,y) #输入簇及对应的标号
Z = clf.decision_function(xy).reshape(axisx.shape) #等于0，超平面，小于-1一类，大于1一类
#画决策边界和平行于决策边界的超平面
ax.contour(axisx,axisy,Z,colors ="k",levels = [-1,0,1],
            alpha = 0.5,linestyles =["--","-","--"])
ax.set_ylim(ylim)
ax.set_xlim(xlim)
#下面这段代码是画出图上某一点与超平面距离相等的所有点组成的平面
plt.scatter(X[10,0],X[10,1],s=20,c="black")
distance = clf.decision_function(X[10].reshape(1,2))
ax.contour(axisx,axisy,Z,colors ="k",levels = [distance],
            alpha = 0.5,linestyles =["-"])
plt.show()