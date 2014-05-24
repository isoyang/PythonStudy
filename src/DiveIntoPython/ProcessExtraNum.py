'''
Created on Dec 9, 2013

@author: yang
'''
labeldata = file('/home/yang/Documents/research/data/all/walkingtest','rb')

labelwrite = open('/home/yang/Documents/research/data/walkingclean','wb')

for row in labeldata.readlines():
    
    rowlist = row.split(',')
    
    lastlist = rowlist[len(rowlist)-1].split('_')
    
    size = len(lastlist)
    
    if size == 3:
        
        number = int(lastlist[len(lastlist)-1])
        if number > -500:
            labelwrite.write(','.join([rowlist[0],lastlist[0]+"_"+lastlist[1]]))
            labelwrite.write('\n')
            
        else:           
            labelwrite.write(row.strip())
            labelwrite.write('\n') 
    else:
        labelwrite.write(row.strip())
        labelwrite.write('\n')        
labeldata.close()
labelwrite.close()
            
        
        