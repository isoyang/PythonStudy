'''
Created on May 21, 2014

@author: yang
'''
import MySQLdb as mdb
import time
import os

path = "/home/yang/Documents/research/data/"

newpath = path+"readyfile/"

conn = mdb.connect(host='localhost',user='root',passwd='mysql')


with conn:
    cursor = conn.cursor()

    conn.select_db('sensordata')

    start = time.time()

    with open(path+'totalfinal','rb') as pair:
    

        for index,val in enumerate(pair.readlines()):
    
            time_list = val.strip().split(",")
    
            count = cursor.execute("SELECt * FROM accelerometer WHERE timestamp >= "+time_list[0]+" and timestamp <= "+time_list[1])
    
            with open(os.path.join(newpath,str(index)+"_"+str(count)),"wb") as datafile:
                
                for content in cursor.fetchall():
                    
                    for i,v in enumerate(content):
                        
                        if i == len(content) - 1:
                            
                            datafile.write(str(v)+"\n")
                        
                        else:
                               
                            datafile.write(str(v)+',')
                    
                
                            print "There are %d records in %d file" % (count,index)

end = time.time() - start
print "Time Consumed: %f" %  end
