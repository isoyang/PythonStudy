'''
Created on May 22, 2014

@author: yang
'''
import os
import gzip

import time

def binarySearch(scIndex,compare,value,blockFind=False):
    
    length = len(scIndex)
    low = 0 
    high = length -1
    
    while low <= high:
        middle = (high-low)/2 + low
        valueloc = scIndex[middle].split(',')
        attrvalue = valueloc[0]
        
        if int(attrvalue) == int(value):
            break
        
        elif int(attrvalue) < int(value):
            
            low = middle + 1
        else:
            high = middle - 1
            
    if low <= high:
        
        if compare == '<=' or compare == '=' or compare == '>=':
            return middle
         
        elif compare == '<':
            
            return middle - 1
        else:
            if middle == length -1:
                
                return -1
            else:
                return middle + 1
            
    else:
        
        if compare == '=':
            return -1
        elif compare == '<' or compare == '<=':
            return high
        
        else:
            if low >= length:
                
                if blockFind:
                    return low - 1
                else:
                    return -1
            else:
                if not blockFind:
                    return low
                else:
                    return high
        
def readIndexBlock(filename,loc,size,home_path):
    
    filepath = os.path.join(home_path,'sorted')
    
    filename = filepath+'/'+filename+".gz"
    
    indexfile = gzip.open(filename, 'rb')
    
    indexfile.seek(int(loc))
    
    return indexfile.read(int(size))

def equalfind(value,compare,home_path,filename):
    
    path = os.path.join(home_path,"secondindex")
    
    scdIndexFile = open(os.path.join(path,filename),'rb')
    
    scIndex = scdIndexFile.read().split('\n')
    scIndex.pop()
    
    satisfylist = []

    index = binarySearch(scIndex,'<=',value,blockFind=True)
    
    if index == -1:
        
        return satisfylist
    
    scIndex[index] = scIndex[index].split(',')
    block = readIndexBlock(filename,scIndex[index][1],scIndex[index][2],home_path)
    blockLines = block.split("\n") 
    blockLines.pop()
    
    lineindex = binarySearch(blockLines,compare,value)
    if lineindex == -1:
        
        return satisfylist
    
    blockAttr = blockLines[lineindex].split(",")
    
    satisfylist += blockAttr
    
    return satisfylist
    
def displayResult(data_path,satisfylist):
    
    rf = open(data_path,'rf')
    
    content = rf.read().split('\n')
    
    for val in satisfylist[1:]:
        
        print content[int(val)]
    
    

if __name__=='__main__':
    home_path='/home/yang/Documents/research/data'
    data_path=home_path+'/all/dataforindex'
    
    result=[]
    start_time = time.time()
    resultlist = equalfind('1371211283','=',home_path,'data_index')
    
    displayResult(data_path,resultlist)
    
    
    
    end_time = time.time()-start_time
    
    print "Time Consumed: %f" % end_time