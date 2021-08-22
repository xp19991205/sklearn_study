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
color = ["blue","red","black"]
for k in range(len(label)):
    plt.scatter(X[k][0],X[k][1],color = color[label[k]])
for k in range(len(centroid)):
    plt.scatter(centroid[k][0],centroid[k][1],color = "yellow",s = 20) #绘制聚类中心
# plt.scatter(inertia)
plt.show()


