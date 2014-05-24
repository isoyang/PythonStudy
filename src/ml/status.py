''
Created on May 15, 2014

@author: yang
'''
import re

ss = "how are (sp?) you? 3.2  >.< I am Fine! Thanks! (: (; :) :$ =) :P :D :o :-) :( =( :@ +o( |-) :-# |-) 8-) :\\ *-) (Y) (N) (U) (^) :] D:> :/"

ss_list = ss.strip().split(" ")

for val in ss_list:
    print val
reg =r'^\(?[\^uyndl8\|+\':;=*>]?[-o\^:\.]?[/<\(\)pdos@\|\$\#\\\]\}]?$'

p = re.compile(reg,re.I)

for value in ss_list:
    
    if p.search(value):
        
        print value,
  

  

  



    
        
    