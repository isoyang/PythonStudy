'''
Created on May 22, 2014

@author: yang
'''
import numpy as np


path = '/home/yang/Documents/research/data/seconddata_fast/0_785'


data_array = np.loadtxt(path+'/1371211318_49',delimiter=',', unpack=False)

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


print mean_matrix








