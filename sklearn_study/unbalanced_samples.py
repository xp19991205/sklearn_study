#这里主要尝试解决的问题是样本数量不均衡的问题
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.datasets import make_blobs
class_1 = 500
class_2 = 50
centers = [[0,0],[2,2]]
cluster_std = [1.5,0.5] #一般来说样本量大的更松散
print(len(centers),len(cluster_std))
X,y =make_blobs(n_samples =[class_1,class_2],centers =centers,cluster_std = cluster_std,random_state=0,shuffle=False)
plt.scatter(X[:,0],X[:,1],c=y,cmap="rainbow",s=10)
# plt.show()
#不设定class_weight
clf = SVC(kernel="linear",C=1)
clf.fit(X,y)
wclf = SVC(kernel="linear",class_weight={1:10}) #注意class_weight输入的是字典
wclf.fit(X,y)
print("score unweighted:{} weighted:{}".format(clf.score(X,y),wclf.score(X,y)))
ax =plt.gca()
ylim = ax.get_ylim()
xlim = ax.get_xlim()
axis_x = np.linspace(xlim[0], xlim[1], 30)  # 在最大最小的坐标上产生取30个点
axis_y = np.linspace(ylim[0], ylim[1], 30)
axisx, axisy = np.meshgrid(axis_x, axis_y)
xy = np.vstack([axisx.ravel(), axisy.ravel()]).T  # 主要功能是把二维数据转为一维
Z_clf = clf.decision_function(xy).reshape(axisx.shape)  # 等于0，超平面，小于-1一类，大于1一类
Z_wclf = wclf.decision_function(xy).reshape(axisx.shape)
a = ax.contour(axisx, axisy, Z_clf, colors="black", levels=[0],
               alpha=0.5, linestyles=[ "-"])
b = ax.contour(axisx, axisy, Z_wclf, colors="red", levels=[0],
               alpha=0.5, linestyles=["-"])
#添加图例：
plt.legend([a.collections[0],b.collections[0]],["non-weighted","weighted"],loc="upper right")
plt.show()
#做了样本均衡后，准确率下降，因为少数类被正确分类的多，而模型整体的预测结果号
#计算Precision:决策边界上方少数点所占比例 （这个值越大，误伤的多数类越少）
precision_clf = (y[y == clf.predict(X)] == 1).sum()/(clf.predict(X) ==1).sum()
precision_wclf = (y[y == wclf.predict(X)] == 1).sum()/(wclf.predict(X) ==1).sum()
print(precision_clf,precision_wclf)
#拆解分析：y == wclf.predict(X) 返回Bool数组预测值等于真实值的y
#如果将多数类判错的代价高昂，那么我们在意整体的准确度，而不是这里的Precision，如果不能放过任何的少数类（增加误判的可能），那么Precision相对低更好

#召回率：衡量少数样本判断正确率 (所有判为少数类的样本数量)/少数类的真实数量
reall_clf = (y[y == clf.predict(X)] == 1).sum()/(y==1).sum()
reall_wclf = (y[y == wclf.predict(X)] == 1).sum()/(y==1).sum()
print(reall_clf,reall_wclf)
#召回率recall 和准确度:precision是两个此消彼长的变量，注意权衡