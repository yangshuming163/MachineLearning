import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets
x = np.array([[1, 1], [3, 3], [4, 3]])
print(x.shape)
y = np.array([0, 1, 2])
print(y.shape)
model =linear_model.LogisticRegression(C=1e5)
model.fit(x, y)
print(model)
print(model.coef_)
print(model.intercept_)
a=np.array([[1,2],[3,4]])

print(help(linear_model.LogisticRegression()))
