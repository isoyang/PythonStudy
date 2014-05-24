'''
Created on May 16, 2014

@author: yang
'''
DATABASE = '/home/yang/Library/data/minidata'
# def loadMetaData
import os,collections,time,gzip

def loadMetaData():
    filename = os.path.join(DATABASE,'meta.table')

    mdfile = open(filename,'rb')
    line = mdfile.readline()

    tablenames = line.strip().split("|")
    tablenames.pop()

    line = mdfile.readline()

    descDic={}

    while line and len(line) > 2:
    
        desc = collections.OrderedDict()
    
        temp = line.strip().split("|")
    
        primary = temp[1].split(" ")[0].split(",")
    
        for i in range(2,len(temp)):
        
            attrDesc = temp[i].split(' ')
        
            while '' in attrDesc:
            
                attrDesc.remove("")
            
            desc[attrDesc[0]] = attrDesc[1]
        
        desc["primary"] = primary
    
        descDic[temp[0]] = desc
        line = mdfile.readline()
        
    return descDic

def lineindex(attrs,tablename,filename,newAll=False):
    
    print 'create index on' , tablename,attrs,filename
    
    rf = open(filename,'r')
    
    wfs = []
    
    path = os.path.join(DATABASE,'index')
    
    if not os.path.isdir(path):
        
        os.mkdir(path)
    
    attrOrders = []
    
    for each in attrs:
        
        attrOrders.append(getAttrOrder(tablename,each))   
        
        wf = open(os.path.join(path,tablename+'_'+each),'w')
        
        wfs.append(wf)
        
    print attrOrders
    
    loc = rf.tell()
    
    line = rf.readline()
    
    lineCount = 0 
    
    countText = ''
    
    while line and len(line) >2:
        
        values = line.strip().split("|")
        
        values.pop()
        
        for i in len(wfs):
            
            wfs[i].write(values[attrOrders[i]]+'\t'+str(lineCount)+'\n')
            
        countText = str(loc)+'\n'
        
        loc = rf.tell()
        
        lineCount += 1
        
        line = rf.readline()
        
    path = os.path.join(DATABASE,'line2loc')
    
    if not os.path.isdir(path):
        
        os.mkdir(path)
        
    fileName = os.path.join(path,filename+"_LINE2LOC.gz")
    
    if not os.path.isdir(fileName):
        
        print time.time()
    
    with gzip.open(fileName, 'wb', compresslevel = 4) as output:
        
        output.write(countText)
        output.flush()
        output.close()
        
    for eachwf in wfs:
        
        eachwf.flush()
        eachwf.close()
        
    rf.close()
        
        
        
        
    
        
        
        
    
    
    




# def getAttrOrder

def getAttrOrder(table,attr):
    
    meta = loadMetaData()
    
    tableDesc = meta[table]
    count = -1

    for k,v in tableDesc.iteritems():

        count += 1
    
        if k == attr:
        
            return count

        
def splitcolumn(tablename,attrname):
    
    tablename = tablename.uppper()
    attrname = attrname.upper()
    
    filename = tablename+'_'+attrname
    
    sc_path = os.path.join(DATABASE,'column')

    if not os.path.isdir(sc_path):
    
        os.mkdir(sc_path)
    
    columnfile = open(os.path.join(sc_path,filename),'wb')

    tablefile = open(os.path.join(DATABASE,'nation.tbl'),'rb')

    line = tablefile.readline()

    while line and len(line) > 0:
    
        record = line.strip().split("|")
        columnfile.write(record[1]+'\n')
        line = tablefile.readline()
    
        columnfile.flush()
        columnfile.close()
        tablefile.close()


    
    


