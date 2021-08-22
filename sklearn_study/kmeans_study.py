from sklearn.datasets import make_blobs #创建几个簇
from matplotlib import pyplot as plt #绘图
X,y = make_blobs(n_samples=500,n_features=2,centers=4,random_state=1) #y代表着簇的标签
fig,ax1 = plt.subplots(1)
ax1.scatter(X[:,0],X[:,1],marker='o',s=8) #s代表点的大小，marker代表绘制点的形状
plt.show()
from sklearn.cluster import k_means #导入kmeans的相关Python包
n_clusters = 3 #选择聚类为3类
cluster = k_means(X,n_clusters = n_clusters,random_state=0)
centroid = cluster[0]
label = cluster[1]
inertia = cluster[2]
print(centroid)
label_name = ["class1","class2","class3"]
plt.figure()
color = ["blue","red","black","orange"]
for k in range(len(label)):
    plt.scatter(X[k][0],X[k][1],color = color[label[k]])
for k in range(len(centroid)):
    plt.scatter(centroid[k][0],centroid[k][1],color = "yellow",s = 20) #绘制聚类中心
# plt.scatter(inertia)
plt.show()
print(inertia) #样本离最近聚类中心的总和

#下面计算轮廓系数 轮廓系数主要衡量的是簇内的距离尽可能小，而簇间距离尽可能大
from sklearn.metrics import silhouette_score #返回平均的一个轮廓系数
from sklearn.metrics import silhouette_samples #返回每个样本的轮廓系数
print(X)
print(silhouette_score(X,label)) #轮廓系数越接近1最好
print(silhouette_samples(X,label)) #每个样本
from sklearn.metrics import calinski_harabasz_score
print(calinski_harabasz_score(X,label)) #每个样本 越大越好