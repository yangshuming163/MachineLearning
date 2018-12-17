import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
def make_meshgrid(x,y,h=0.2):
    x_min,x_max = x.min()-1,x.max()+1
    y_min,y_max = y.min()-1,y.max()+1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    return xx, yy

def load_data():
    iris = datasets.load_iris()
    x = iris.data[:, :2]
    y = iris.target

def plot_contours(ax,clf,xx,yy,**params):
    z=clf.predict(np.c_[xx.ravel(),yy.ravel()])
    z=z.reshape(xx.shape)
    out =ax.contourf(xx, yy,z, **params)
    return out

