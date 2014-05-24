'''
Created on May 16, 2014

@author: yang
 
'''
filename = 'db'
tablename = 'nation'

str1 = filename+'\n'+tablename

with open('/home/yang/minidb_test.txt','wb') as ot:
    
    ot.write(str1)
    ot.flush()
    ot.close()