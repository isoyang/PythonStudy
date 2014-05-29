'''
Created on May 29, 2014

@author: yang
'''
import MySQLdb as mdb
import time
import os

path = "/home/yang/Documents/research/data/"
data_path = os.path.join(path,'data_one_file')
loc_path = os.path.join(path,data_path+'/loc')
print loc_path

conn = mdb.connect(host='localhost',user='root',passwd='mysql')

with conn:
    
    cursor = conn.cursor()
    conn.select_db('sensordata')
    
    with open(os.path.join(path,'totalfinal'),'rb') as pair:
        
        for index, value in enumerate(pair.readlines()):
            time_list = value.strip().split(',')
            count = cursor.execute("SELECt * FROM accelerometer WHERE timestamp >= "+time_list[0]+" and timestamp <= "+time_list[1])
            