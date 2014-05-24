'''
Created on May 22, 2014

@author: yang
'''
import MySQLdb as mdb
import time
import os

path = "/home/yang/Documents/research/data/"


conn = mdb.connect(host='localhost',user='root',passwd='mysql')


with conn:
    
    cursor = conn.cursor()

    conn.select_db('sensordata')

    start = time.time()
    
    
    for fil in os.listdir(os.path.join(path,"secondfile")):
        
        if "auto" in fil:
            
            print "this is a script file!!"
            continue
        print "################# %s ####################" % fil
        with open(os.path.join(path,"secondfile",fil),'rb') as second:
            
            for val in second.readlines():
                
                print val
                val = val.strip()
                
                sql = "select x,y,z from accelerometer where timestamp = "+str(val)
                count = cursor.execute(sql)
                
                data_dir = os.path.join(path,"seconddata_fast",fil)
                
                if not os.path.isdir(data_dir):
                    
                    os.makedirs(data_dir)
                                    
                with open(os.path.join(data_dir,val+"_"+str(count)),'wb') as datafile:
                    
                    for content in cursor.fetchall():
                        
                        for i,con in enumerate(content):
                            
                            if i == len(content) - 1:
                            
                                datafile.write(str(con)+"\n")
                        
                            else:
                               
                                datafile.write(str(con)+',')
                    
                    

end = time.time() - start
print "Time Consumed: %f" %  end
                    
                    
            
            