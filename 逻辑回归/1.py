import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets
#读取sklearn 中的数据集
iris = datasets.load_iris()

#读取数据前两列的内容
x= iris.data[:, :2]

y= iris.target

model = linear_model.LogisticRegression(C=1e5)
model.fit(x, y)
#权重
print(model.coef_)
#截距
print(model.intercept_)
h=.02
x_min, x_max =x[:, 0].min() - .5, x[:, 0].max() + .5
y_min, y_max =x[:, 1].min() - .5, x[:, 1].max() + .5

#创建等差数组
hh=np.arange(x_min, x_max, h)
print(hh)
hhh=np.arange(y_min, y_max, h)
print(hhh)
xx, yy = np.meshgrid(hh, hhh)
print(xx)
print(xx.shape)
print(yy)
print(yy.shape)
xx1=xx.ravel()
yy1=yy.ravel()
print(xx1.shape)
print(xx1)
print(yy1.shape)
print(yy1)
#p=[1,2,3]
#q=[4,5,6]
#m=np.c_[p,q]
#n=np.r_[p,q]
#print(m)
#print(n)
np_c=np.c_[xx1,yy1]
print(np_c)
predict = model.predict(np_c)
print(predict)
print(predict.shape)
predict = predict.reshape(xx.shape)
print(predict)
plt.figure(1, figsize=(8, 6))
plt.pcolormesh(xx, yy, predict, cmap=plt.cm.Paired)
plt.scatter(x[:, 0], x[:, 1], c=y, edgecolors='k', cmap=plt.cm.Paired)
plt.xlabel('length')
plt.ylabel(' width')
plt.show()

a=np.zeros((5,2))
print(type(a))

