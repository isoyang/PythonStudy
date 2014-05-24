'''
Created on Dec 9, 2013

@author: yang
'''
labeldata = file('/home/yang/Documents/research/data/walklabelrevised.csv','rb')

dellabel = open('/home/yang/Documents/research/data/test.csv','wb')


testlist = labeldata.readlines()
pointer = 1
size = len(testlist)

print type(testlist)

dellabel.write(testlist[0])

print testlist[1::1]
  

for row in testlist[1:size-1]:
    
        if ('START' in row and 'START' in testlist[pointer-1]) or ('STOP' in row and 'STOP' in testlist[pointer+1]):
            pointer+=1
            continue
        dellabel.write(row)
        pointer+=1
       
dellabel.write(testlist[size-1])         
    
         
    
    
        
    
    
            
            
        
        
    
        
      
    