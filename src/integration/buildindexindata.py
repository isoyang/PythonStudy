'''
Created on May 22, 2014

@author: yang
'''
import os
import gzip
import collections


def buildcolumnindex(attr,filename,home_path):
    
    rf = open(filename,'rb')
    
    path = os.path.join(home_path,'index')
    
    if not os.path.isdir(path):
        
        os.mkdir(path)
        
    wf = open(os.path.join(path,'data_index'),'w')
    
    loc = rf.tell()
    
    line = rf.readline()
    
    lineCount = 0
    
    countText = ''
    
    while line and len(line) > 2:
        
        values = line.strip().split(",")
        
        values.pop()
        
        wf.write(values[attr]+','+str(lineCount)+'\n')
        
        countText += str(loc)+'\n'
        
        loc = rf.tell()
        
        lineCount += 1
        
        line = rf.readline()
        
    path = os.path.join(home_path,'line2loc')
    
    if not os.path.isdir(path):
        
        os.mkdir(path)
        
    fileName = os.path.join(path,"LINE2LOC.gz")
    
    if not os.path.isfile(fileName):
        
      
        with gzip.open(fileName, 'wb', compresslevel = 4) as output:
        
            output.write(countText)
            output.flush()
            output.close()    
    wf.flush()    
    wf.close()
    rf.close()   

def buildindex(filename,home_path,blocksize):
    
    dic = collections.defaultdict(list)
    path = os.path.join(home_path,'index')
    pathfile = os.path.join(path,filename)
    rf = open(pathfile,'r')
    line = rf.readline()
    
    print "Begin to Read index file.........."
    while line and len(line) > 2:
    
        line = line.strip()
        vkpair = line.split(',')
        key = vkpair[0]
        dic[key].append(vkpair[1])

        line = rf.readline()
    print "Reading File has been done!"   
    tuple_list = dic.items() 
    li = sorted(dic.items(),key=lambda tuple_list: tuple_list[0])  
    
    scddir = os.path.join(home_path,"secondindex")
    if not os.path.isdir(scddir):
        os.mkdir(scddir)
    scwf = open(os.path.join(scddir,filename),"w")
    
    sortdir = os.path.join(home_path,"sorted")
    if os.path.isdir(sortdir) == False:
        os.mkdir(sortdir)    
    wf = gzip.open(os.path.join(sortdir,filename+".gz"),'wb',compresslevel = 4)
    
    block = ""
    newblock = True
    endloc=0
    print "Begin to write Blocks!!!"
    for k in li:
        if newblock:
            blockattr = str(k[0])
            newblock = False
            
        line = str(k[0])+","
        
        for index,loc in enumerate(k[1]):          
            if index == len(k[1]) - 1:               
                line += loc
            else:
                line += loc+","
                
        line = line.strip()
        block += line+"\n"
        
        if len(block) > blocksize:
            startloc = endloc
            wf.write(block)
            endloc = wf.tell()
            size = endloc - startloc
            scwf.write(blockattr+","+str(startloc)+","+str(size)+'\n')
            block = ""
            newblock = True  
    
    startloc = endloc
    wf.write(block)
    endloc = wf.tell()
    size = endloc - startloc
    scwf.write(blockattr+','+str(startloc)+','+str(size)+'\n')
    print "Writing Blocks has been done!!"
    scwf.flush()  
    scwf.close()
    wf.flush()  
    wf.close()
       
    
if __name__ == '__main__':
    
    home_path = '/home/yang/Documents/research/data'
    
    #buildcolumnindex(0,home_path+'/all/dataforindex',home_path)  
    buildindex("data_index",home_path,32)
        
    
    