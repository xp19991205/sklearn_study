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
X = StandardScaler().fit_transform(X)
#划分训练集，测试集
X_train,X_test,Y_train,Y_test = train_test_split(X,y,test_size=0.3,random_state=420)
score = []
gamma_range = np.logspace(-10,5,100) #start,stops,numbers
for k in gamma_range:
    clf = SVC(kernel="rbf",gamma=k,cache_size=5000).fit(X_train,Y_train)
    score.append(clf.score(X_test,Y_test))

plt.plot(gamma_range,score)
plt.show()
index = score.index(max(score))
print("max_score = {} index = {} value = {}".format(max(score),index,gamma_range[index]))

from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV #带交叉验证的网格搜索
time0 = time()
gamma_range = np.logspace(-10,5,50) #start,stops,numbers
coeff_range = np.linspace(0,5,10) #start,stops,numbers
#总共的循环次数为50*10=500次
param_grid = dict(gamma=gamma_range,coef0 = coeff_range)
cv = StratifiedShuffleSplit(n_splits=5,test_size=0.3,random_state=420)
grid = GridSearchCV(SVC(kernel="poly",degree=1,cache_size=5000),param_grid = param_grid,cv = cv)
grid.fit(X,y)
best_param = grid.best_params_
best_score =grid.best_score_
print(best_param)
print("最优参数{} score ={}".format(best_param,best_score))