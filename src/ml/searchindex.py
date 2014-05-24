'''
Created on May 16, 2014

@author: yang
'''
import os,struct,math,time,sys

start_time = time.time()
file_path = '/home/yang/Pictures/index.dat'

eps = 26

ip = '3758096383'

index_size = os.path.getsize(file_path)

index = open(file_path,'rb')

begin = 0 
offset = 0 
length = 0

indicator = 0

line = 'This is a Test'
end = index_size

print "##############  The Search Has Begin ! #######################"
while (True):
    
    if (end - begin) > eps :
        
        indicator += 1
    
        middle_offset = begin + math.ceil(((end - begin)/eps)/2)*eps
    
        index.seek(middle_offset)
    
        middle_ip = struct.unpack('L',index.read(8))[0]
        
    
        if float(ip) > float(middle_ip):
                   
            begin = middle_offset
            
            print "Iteration of Searching %d:  Target IP: %s > Middle IP: %s" %(indicator,ip,middle_ip)
            print ''
    
        else:
                   
            end = middle_offset
            
            print "Iteration of Searching %d: Target IP < Middle IP" % indicator
            print ''
    else:
        print '-------------------Target Interval Has Been Identified !-------------------'
        print ''
        break
# Target Interval has been identified             
index.seek(begin)
        
s_ip = struct.unpack('L',index.read(8))[0]
        
e_ip = struct.unpack('L',index.read(8))[0]
        
if float(ip) < float(s_ip) or float(ip) > float(e_ip):
            
    print "The Target has been out of identified interval"
    sys.exit(1)

offset = struct.unpack('L',index.read(8))[0]

length = struct.unpack('H',index.read(2))[0]

              
if length > 0:
    
    index.close()
    
    realdata = open('/home/yang/Desktop/ip-to-country.csv','rb')
    
    realdata.seek(offset)
    
    line = realdata.read(length)

end_time = time.time() - start_time

print "################################# Target Has Been Found ############################"
print "Target Record: %s" % line
print "%d Iterations In Total" % indicator
print "Time consumed: %f" % end_time
