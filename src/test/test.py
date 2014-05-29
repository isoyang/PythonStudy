'''
Created on May 23, 2014

@author: yang
'''
# test function seek()
import os

# file_loc = '/home/yang/Documents/research/data/all/dataforindex'
# 
# fstream = open(file_loc,'rb')

#print fstream.tell()

# reach the end of file 
# default os.SEEK_SET  from start    os.SEEK_CUR move relative to current  os.SEEK_END move relative to end of file 
#fstream.seek(0,os.SEEK_END)

#print fstream.tell()

# line = fstream.readline()
# i = 1
# while i < 8:
#     
#     print fstream.tell(), '######',line
#     
#     print '_______________'
#     
#     i +=1
#     line = fstream.readline()
#     
#     
# print 100/6
# 
# print "Set Github Ready!!"
#     
path = '/home/yang/Documents/research/data/seconddata_fast/0_785'

file_list = os.listdir(path)

print file_list

f = sorted(file_list,key = lambda x: x.split('_')[0])


print f


