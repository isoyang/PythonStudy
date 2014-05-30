'''
Created on May 22, 2014

@author: yang
'''
import numpy as np
import scipy as sp


path = '/home/yang/Documents/research/data/seconddata_fast/0_785'


data_array = np.loadtxt(path+'/1371211318_49',delimiter=',', unpack=False)

def cal_coff(array,indicator):
    
    axis = indicator == 0;
    if axis:
        length = array.shape[1]
    else:
        
        length = array.shape[0]
        
    for x in xrange(0,length):       
        for y in xrange(0,length):            
            if x != y :               
                if axis:                    
                    yield sp.corrcoef(array[:,x], array[:,y])
                else:
                    yield sp.corrcoef(array[x,:], array[y,:])

data_matrix = np.matrix(data_array)

print data_matrix[:,0].shape
array_max = np.max(data_array, axis=0)
print array_max.shape
array_min = np.min(data_array, axis=0)
array_mean = np.mean(data_array,axis=0)
array_var = np.var(data_array, axis=0)
array_std = np.std(data_array, axis=0)

# along column 
print "mean of data_array:     %s"  % array_mean
print "maximum of data_array:  %s" %  array_max
print "minimum of data_array:  %s"  % array_min
print "variance of data_array: %s"  % array_var
print "standard deviation  of data_array: %s"  % array_std

# transpose of one dimensional array
array_mean_t = np.transpose(array_mean)
# create mean matrix

mean_matrix = np.dot(np.ones((49,1)),array_mean.reshape(1,3))

def cal_feature(array,indicator,string):
    
    dot_array = array*array
    if string == 'rms':
        
        return np.sqrt(np.sum(dot_array, axis=indicator)/array.shape[indicator])
    elif string == 'svm':
        
        return np.sum(np.sqrt(np.sum(dot_array, axis=indicator)))/array.shape[1-indicator]              


test_array = np.array([[1,2],[3,4],[5,6],[0,0]])
print test_array
array_str=np.array2string(test_array)

#  slice matrix

cc = test_array[:,0]


print np.sum(np.nonzero(cc))

# normalized
t_mean = np.mean(test_array,axis=0)
t_std = np.std(test_array,axis=0)


print t_mean.reshape(1,-1).shape
print t_std

mean_matrix = np.dot(np.ones((4,1)), t_mean.reshape(1,-1))

std_matrix = np.dot(np.ones((4,1)),t_std.reshape(1,-1))

print std_matrix

normalised_data = (test_array-mean_matrix)/std_matrix

print np.std(normalised_data,axis=0)

if 0 in test_array:
    
    print 'TRUE'











