import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split,cross_val_score,cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn import metrics
data=pd.read_csv('Folds5x2_pp.csv')
#打印前五行
print(data.head())
#打印数据的类型
print(data.shape)
#准备样本特征
x=data[['AT','V','AP','RH']]
#准备输出特征
y=data['PE']
print(type(x))
x_train, x_test, y_train, y_test = train_test_split(x, y,random_state=1)
print(type(x_train))
print(x_train.shape)
print(x_test.shape)
model=LinearRegression()
model.fit(x_train,y_train)
print(model.intercept_)
print(model.coef_)
#评分函数
score=model.score(x_test,y_test)
print(score)
#交叉验证
scores=cross_val_score(model,x,y)
print(scores.mean())
#用均方差评估模型
y_pred = model.predict(x_test)
mse=metrics.mean_squared_error(y_test, y_pred)
print(mse)
predicted = cross_val_predict(model, x, y, cv=10)
#画图表示真实值和预测值的关系
fig, ax = plt.subplots()
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.scatter(y,predicted)
plt.show()
print((11.80*-1.97376045+40.66*-0.23229086+1017.13*0.0693515+97.20*-0.15806957)+447)
