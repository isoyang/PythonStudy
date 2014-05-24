'''
Created on Dec 9, 2013

@author: yang
'''

labeldata = file('/home/yang/Documents/research/data/all/walking','rb')

combinewalk = open('/home/yang/Documents/research/data/combine/walk.csv','wb')

for row in labeldata.readlines()[1:]:

    print row
    
    
    