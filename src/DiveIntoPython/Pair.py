'''
@author: yang
'''

maindata = file('/home/yang/Documents/research/data/walkingclean','rb')

labelwrite = open('/home/yang/Documents/research/data/walkingcleantest','wb')

arraylist = [];

for row in  maindata.readlines():
    
    arraylist.append(row);

indicator = [];

for index,item in enumerate(arraylist):
      
    if "STOP" in item  and "START" in arraylist[index-1]:
        
        indicator.append(index+1)
    
    elif "START" in item and "STOP" in arraylist[index+1]:
        indicator.append(index+1)



for num in indicator:
    
    labelwrite.write(str(num))
    labelwrite.write('\n')

maindata.close()
labelwrite.close()
         
        