'''
Created on May 29, 2014

@author: yang
'''
import os
import numpy as np 
import scipy as sp

path = "/home/yang/Documents/research/data/seconddata_fast/"

data = open('/home/yang/Documents/research/data/data_one_file/normalized_data_file','wb')
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

def cal_feature(array,indicator,string):
    
    dot_array = array*array
    if string == 'rms':
        
        return np.sqrt(np.sum(dot_array, axis=indicator)/array.shape[indicator])
    elif string == 'svm':
        
        return np.sum(np.sqrt(np.sum(dot_array, axis=indicator)))/array.shape[1-indicator]              
   
def construct_features(array,pointer):
    # pointer = 0 means  array n*d
    # pointer = 1 means  array d*n
    # feature_list=[x_y_z_mean, x_y_z_max,x_y_z_min, x_y_z_max, x_y_z_std, x_y_z_rms, array_svm]
    array_svm = cal_feature(array,1-pointer,'svm')
      
    feature_list = list(np.mean(array,axis=pointer))+list(np.max(array, axis=pointer))+list(np.min(array, axis=pointer))+list(np.std(array, axis=pointer))+list(cal_feature(array,pointer,'rms'))
    
    feature_list.append(array_svm)
    
    return np.array(feature_list)

def normalized(array,pointer):
    
    array_mean = np.mean(array,axis=pointer)
    array_std = np.std(array,axis=pointer)
    denominator = np.dot(np.ones((len(array),1)),array_std.reshape(1,-1))
    
    if 0 in denominator:
        
        print "Divide is not possible!!!!"
        return (array-np.dot(np.ones((len(array),1)),array_mean.reshape(1,-1)))
        
    else:
        
        return (array-np.dot(np.ones((len(array),1)),array_mean.reshape(1,-1)))/denominator
 
        
        
def construct_svm_features(array,pointer):
    
    array_svm = cal_feature(array,1-pointer,'svm')
    
    feature_list = list(np.max(array, axis=pointer)-np.min(array, axis=pointer))+list(np.max(array, axis=pointer))+list(np.min(array, axis=pointer))+list(np.median(array, axis=pointer))

    feature_list.append(array_svm)
    
    return feature_list
def write2file(file,array):
    
    for index,val in enumerate(array):
        
        if index == len(array) - 1:
            
            file.write(str(val)+'\n')
             
        else:
            
            file.write(str(val)+',')
    
list_dir = os.listdir(path)
pair_dir = [path+val for val in list_dir]
interval = 3
location_list = []
feature_list = []

for index,val in enumerate(pair_dir):
    file_name_list = sorted(os.listdir(val),key = lambda x: x.split("_")[0])
    length = len(file_name_list)
    print "########## There are %d seconds in %s" % (length,val)
    if length < interval:
        
        print "This directory has not enough seconds!!"
        continue
    num = length/interval
   
    print "##########  %d feature records will be constructed  #############" % num
    file_list = [os.path.join(val,file_name) for file_name in file_name_list]
    
    for val in xrange(0,length,interval):
        total_array=[]
        if val+interval > length:          
            print "There are no enough seconds for features!!!"
            break           
        for n in xrange(val,val+interval):          
            with open(file_list[n],'rb') as content:                
                for value in content.readlines():
                    total_array.append(value.strip().split(','))                    
            
        flist=construct_svm_features(normalized(np.array(total_array,np.float),0),0)
        write2file(data,flist)         
data.close()      
    
    
        
        
    
    
                                                                                                           
    
    




