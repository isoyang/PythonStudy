'''
Created on May 29, 2014

@author: yang
'''
import numpy as np
from sklearn import datasets
#from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
#from sklearn import linear_model
from sklearn import svm

def normalized(array,pointer):
    
    array_mean = np.mean(array,axis=pointer)
    array_std = np.std(array,axis=pointer)
    denominator = np.dot(np.ones((len(array),1)),array_std.reshape(1,-1))
    
    if 0 in denominator:
        
        print "Divide is not possible!!!!"
        return (array-np.dot(np.ones((len(array),1)),array_mean.reshape(1,-1)))
        
    else:
        
        return (array-np.dot(np.ones((len(array),1)),array_mean.reshape(1,-1)))/denominator
 

def readfromfile(filename):
    final_list=[]
    with open(filename,'rb') as file_con:
        
        for value in file_con.readlines():
            
            if value:
                
                value_list = value.strip().split(',')
                final_list.append(value_list)
    return np.asarray(final_list)

data = np.loadtxt('/home/yang/Documents/research/data/data_one_file/normalized_data_file',dtype=np.float,delimiter=',',unpack=False)

length = len(data)

data = normalized(data,0)
data_y = np.ones(length)

np.random.seed(0)
indices = np.random.permutation(length)
 
data_train = data[indices[:-1000]]
data_y_train = data_y[indices[:-1000]]
data_test = data[indices[-1000:]]
data_y_test = data_y[indices[-1000:]]

# PCA DEcomposition

# pca = PCA(n_components=5)
# data_train_new = pca.fit_transform(data_train)
# data_test_new = pca.fit_transform(data_test)
# print(pca.explained_variance_ratio_)
# knn = KNeighborsClassifier(n_neighbors=10)
# knn.fit(data_train, data_y_train)
# data_y_target = knn.predict(data_test)

# logistic = linear_model.LogisticRegression(C=1e5)
# logistic.fit(data_train,data_y_train)
# data_y_target = logistic.predict(data_test)
# print data_y_target
# multiple chocice
accuracy=[]
for x in [0.015,0.1,0.4]:
    
    ocsvm = svm.OneClassSVM(nu=x,gamma=x)
    ocsvm.fit(data_train)
    data_y_target = ocsvm.predict(data_test)
    correct_rate = (1-len(np.nonzero(data_y_test - data_y_target)[0])/float(len(data_y_target)))
    accuracy.append(correct_rate)
    
print accuracy



