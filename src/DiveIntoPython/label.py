'''


@author: yang
'''

labelfile = file ("/home/yang/Documents/research/data/totalfinal","rb")
datafile = file ("/home/yang/Documents/research/data/timestamp","rb")
 
datafilelist=[]

for d in datafile.readlines():
    datafilelist.append(d.strip())
     
 
labeleddata = open ("/home/yang/Documents/research/data/labeldata","wb")
labeledname = open ("/home/yang/Documents/research/data/namedata","wb")

namelist=[]
datalist=[]

for line in labelfile.readlines():
    
    linearray = line.strip().split(",")
    
    left=linearray[0]
    right=linearray[1]
    
    print   linearray
    
    for row in datafilelist:
         
        row=row.strip()
        if int(row) < int(left) or int(row) > int(right):
             
             
            continue
         
        else:
            print row
            namelist.append(row)
             
            if int(row) > int(left) and int(row) < int(right):
             
                datalist.append("WALKING")
             
            elif int(row) == int(left):
             
                datalist.append("WALKING_START")
            
            elif int(row) == int(right):
                datalist.append("WALKING_STOP")
             
     
#===============================================================================
         
for dataline in datalist:
     
    labeleddata.write(dataline)
    labeleddata.write('\n')     
         
for dataline in namelist:
     
    labeledname.write(dataline)
    labeledname.write('\n') 
 
datafile.close()
labeleddata.close()
labeledname.close()
           
    