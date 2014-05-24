'''
Created on May 16, 2014

@author: yang
'''
import struct
#from buildindex import print_list
binarydata = open('/home/yang/Pictures/index.dat','rb')

types = 'LLLH'
size = struct.calcsize(types)
"""
while(True):
    
    stream = binarydata.read(size)
    
    if not stream:
        
        break
    result = struct.unpack(types,stream)

    print_list(result)
"""
offset = 26

binarydata.seek(2*offset)

(a,b,c,d) = struct.unpack('LLLH',binarydata.read(offset))

print a,b,c,d

real = open('/home/yang/Desktop/ip-to-country.csv','rb')

real.seek(int(c))

line = real.read(int(d))

print line,

binarydata.close() 
real.close()