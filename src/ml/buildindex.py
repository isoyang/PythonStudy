import struct
filedata=open('/home/yang/Desktop/ip-to-country.csv','rb')
indexdata=open('/home/yang/Pictures/index.dat','wb')


def print_list(lis):
    
    for val in lis:
        
        print val,
    print ""

offset = 0 
for dex,line in enumerate(filedata.readlines()):
    print dex
    strlen = len(line)
    line_list = line.strip().split(",")
    
    start_ip = float(line_list[0])
    end_ip = float(line_list[1])
    
    index = struct.pack('LLLH',start_ip,end_ip,offset,strlen)
    
    indexdata.write(index)
    
    offset += strlen
 
filedata.close()
indexdata.close()