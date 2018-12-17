import numpy as np
from sklearn.svm import SVC
x = np.array([[1, 1], [3, 3], [4, 3]])
y = np.array([1, 2, 2])
clf = SVC()
clf.fit(x,y)

print(clf.predict([[2, 2.1]]))