'''
Created on May 23, 2014

@author: yang
'''
from time import time 

t = time() 
s = ""
alist = ['a','b','b','d','e','f','g','h','i','j','k','l','m','n'] 


s = "".join(alist)  

print s
print "total run time:"
print time()-t