from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
def load_data():
    iris=datasets.load_iris()
    print(iris.data.shape)
    print(iris.target.shape)
    x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.1,random_state=0)
    print(x_train.shape)
    print(x_test.shape)
    return x_train,x_test,y_train,y_test

def testLiner_SVC(x_train,x_test,y_train,y_test):
    clf=svm.LinearSVC()
    clf.fit(x_train,y_train)
    print(clf.coef_,clf.intercept_)
    print(clf.score(x_test,y_test))

if __name__=="__main__":
    x_train,x_test,y_train,y_test=load_data()
    testLiner_SVC(x_train,x_test,y_train,y_test)