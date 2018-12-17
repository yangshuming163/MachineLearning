#!/usr/bin/python
# -*- coding: utf-8 -*-
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.externals.six import StringIO
from sklearn.model_selection import train_test_split,cross_val_score

import pydotplus
dot_data = StringIO()
iris=load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target,random_state=1)
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x_train,y_train)
score=clf.score(x_test,y_test)
print(score)
dot_data = StringIO()
tree.export_graphviz(clf,
                        out_file=dot_data,
                        feature_names=iris.feature_names,
                        class_names=iris.target_names,
                        filled=True,rounded=True,
                        impurity=False)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# 输出pdf，显示整个决策树的思维过程
graph.write_pdf("viz.pdf")