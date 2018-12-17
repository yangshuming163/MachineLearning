import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split,KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score
data=pd.read_csv('creditcard.csv')
#对数据进行预处理
l=np.array(data['Amount']).reshape(-1,1)
data['normAmount'] = StandardScaler().fit_transform(l )

print(data['normAmount'])
#删除列，axis默认为0是删除行，列是1
data=data.drop(['Time','Amount'],axis=1)
#print(data.head())
X = data.ix[:, data.columns != 'Class']
y = data.ix[:, data.columns == 'Class']
number=len(data[data['Class']==1])
#print(number)
#返回下标值
fraud_indices=np.array(data[data['Class']==1].index)
normal_indices=(data[data['Class']==0]).index
#print(normal_indices)
#下采样，把多的行数变成和少的行数一样
random_normal_indices=np.random.choice(normal_indices,number,replace=False)
#print(random_normal_indices)
random_normal_indices=np.array(random_normal_indices)
#print(random_normal_indices)
#把两个下标合并一起
under_sample_indices=np.concatenate([fraud_indices,random_normal_indices])
#print(len(under_sample_indices))
#iloc 在index的位置上进行索引,不包括end  loc 在index的标签上进行索引,范围包括start和end。
#data.iloc[:2,:]是前两行 ，loc[:2,:]是到0到2这个下标值的行数
under_sample_data=data.iloc[under_sample_indices,:]
#print(under_sample_data)
X_sample=under_sample_data.ix[:,under_sample_data.columns!='Class']
Y_sample=under_sample_data.ix[:,under_sample_data.columns =='Class']
#print(len(Y_sample[Y_sample.values==1])/(len(Y_sample[Y_sample.values==1])+len(Y_sample[Y_sample.values==0])))
#random_state=0 保证每次运行切分出的数据不会变
X_train,X_test,y_train,=train_test_split(X,y,test_size=0.3,random_state=0)
X_train_undersample,X_test_undersample,y_train_undersample,y_test_undersample=train_test_split(X_sample,Y_sample,test_size=0.3,random_state=0)
print(X_train_undersample)

def printing_Kfold_scores(x_train_data,y_train_data):
    fold=KFold(5,shuffle=False)
    c_param_range=[0.01,0.1,1,10,100]
    results_table = pd.DataFrame(index=range(len(c_param_range), 2), columns=['C_parameter', 'Mean recall score'])
    results_table['C_parameter'] = c_param_range
    j=0
    for c_param in c_param_range:
        print('-------------------------------')
        print('C parameter:',c_param)
        print('-------------------------------')
        print('')
        recall_accs=[]
        #fold.split(x_train_data)返回两个值 一个是交叉验证的测试集，一个是交叉验证是验证集
        #indices[0]为测试集的下标值，indices[1]为验证集的下标值
        for iteration,indices in enumerate(fold.split(x_train_data),start=1):
            lr = LogisticRegression(C=c_param, penalty='l1')
            lr.fit(x_train_data.iloc[indices[0], :], y_train_data.iloc[indices[0], :].values.ravel())
            y_pred_undersample = lr.predict(x_train_data.iloc[indices[1], :].values)
            recall_acc = recall_score(y_train_data.iloc[indices[1], :].values, y_pred_undersample)
            recall_accs.append(recall_acc)
            print('Iteration ', iteration, ': recall score = ', recall_acc)
        results_table.ix[j, 'Mean recall score'] = np.mean(recall_accs)
        j += 1
        print('')
        print('Mean recall score ', np.mean(recall_accs))
        print('')
    print(results_table)


#best_c = printing_Kfold_scores(X_train_undersample,y_train_undersample)
#过采样
credit_cards=pd.read_csv('creditcard.csv')
columns=credit_cards.columns

features_columns=columns.delete(len(columns)-1)
features=credit_cards[features_columns]
labels=credit_cards['Class']
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)
print(len(features_train))
oversampler=SMOTE(random_state=0)
os_features,os_labels=oversampler.fit_sample(features_train,labels_train)
print(len(os_features))
os_features = pd.DataFrame(os_features)
os_labels = pd.DataFrame(os_labels)
#printing_Kfold_scores(os_features,os_labels)

lr = LogisticRegression(C = 1, penalty = 'l1')
lr.fit(os_features,os_labels.values.ravel())
y_pred = lr.predict(features_test.values)
recall_acc = recall_score(labels_test, y_pred)
print(recall_acc)