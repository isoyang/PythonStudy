'''
Created on Oct 31, 2013

@author: yang
'''
'''
import os

for filename in os.listdir('/home/yang/Documents/Work/Excel'):
    
    print filename
    

import glob

for filename in  glob.glob('/home/yang/Documents/Work/Excel/*.xls'):
    
    print filename


import os.path

def processDirectory (args,dirname,filenames):
    f =re open("/home/yang/Desktop/test.txt","w")
    print >> f, 'Directory', dirname
    for filename in filenames:
        print >> f, ' File',filename

os.path.walk('/home/yang/Documents/Work/Excel', processDirectory, None)   

'''
'''
import csv

csvfile = file('/home/yang/Documents/research/data/all/Accelerometer.csv','rb')

reader = csv.reader(csvfile)

csvwrite = open('/home/yang/Documents/research/data/modifieddata/modified.csv','wb')

writer = csv.writer(csvwrite,dialect='excel')

pointer = 1

for line in reader:
    
        size = len(line)
        newlist = [line[2],line[4],line[size-3],line[size-2],line[size-1]]
        
        writer.writerow(newlist)
       
        print pointer
        
        pointer+=1
        
csvfile.close()
csvwrite.close()
'''
'''
import csv

newfile = file('/home/yang/Documents/research/data/all/org.sizzlelab.contextlogger.android.CustomProbe.ApplicationProbe.csv','rb')

newfile1 = open('/home/yang/Documents/research/data/modifieddata/modifiedlabel.csv','wb')

reader = csv.reader(newfile)
csvwrite = csv.writer(newfile1,dialect='excel')

indicator = 1

for line in reader:
    
    csvwrite.writerow([line[2],line[3]])
    print indicator
    
    indicator = indicator + 1
    
newfile.close()
newfile1.close()
'''    
    

import csv

label = file('/home/yang/Documents/research/data/modifieddata/modifiedlabel.csv','rb')

walklabel = open('/home/yang/Documents/research/data/walklabel.csv','wb')

reader = csv.reader(label)
writer = csv.writer(walklabel,dialect='excel')


for line in reader:
    
    if 'WALKING' in line[len(line)-1] or reader.line_num == 1:
        
        writer.writerow(line)
        
label.close()
walklabel.close()
       
        
        
        

