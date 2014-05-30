'''
Created on May 30, 2014

@author: yang
'''
import os

#total label file
state='jogging'
path = '/home/yang/Documents/research/data'
label_loc = os.path.join(path,'all/org.sizzlelab.contextlogger.android.CustomProbe.ApplicationProbe.csv')

# select label
w_file = open(os.path.join(path,'label/'+state),'wb')

def printList(li):
    
    for val in li:
        
        print val
def getList(filename,state):   
    # store label infomation
    data_list = []
    #open file
    with open(filename,'rb') as label:
    
        for value in label.readlines()[1:]:
        
            value = value.strip().split(',')
        
            if state.upper() in value[3]:
                data_list.append([value[2],value[3]])
        
    return data_list       

def processNum(li):
    new_list = []
    indicator = False
    for index,record in enumerate(li):
        
        if indicator:          
            continue
        label_list = record[1].split('_')
        
        if len(label_list) == 3:
            
            if int(label_list[len(label_list)-1]) > -500:
                record[1] = '_'.join([label_list[0],label_list[1]])
                new_list.append(record)
                
            else:
                if 'STOP' in record[1] and index != 0:
                    new_list.pop()
                
                elif 'START' in record[1] and index < len(li)-1:
                    
                    indicator = True
                                        
        else:
            new_list.append(record)
            
            
    return new_list

def removeDuplicate(li):
    
    new_list = []
    pointer = 1
    for value in li[1:len(li)-1]:
        
        if ('START' in value and 'START' in li[pointer-1]) or ('STOP' in value and 'STOP' in li[pointer+1]):
            pointer+=1
            continue
        new_list.append(value)
        pointer+=1
    return new_list   
if __name__ == '__main__':
    
    data = getList(label_loc,state)
    printList(data)
    data = processNum(data)
    printList(data)
   






