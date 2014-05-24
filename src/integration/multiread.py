'''
Created on May 23, 2014

@author: yang
'''
import time
import os
import multiprocessing as mp

WORKERS = 4
BLOCK_SIZE = 0
FILE_NAME = '/home/yang/Documents/research/data/all/dataforindex'
FILE_SIZE = 0 


def getFileSize(file):
    
    global FILE_SIZE
    fstream = open(file,'rb')
    fstream.seek(0,os.SEEK_END)
    FILE_SIZE = fstream.tell()
    fstream.close()
   

def process(pid,array,rclock):
    
    global FILE_SIZE,BLOCK_SIZE
  
    try:
        fs = open(FILE_NAME,'rb')
        rclock.acquire()
        begin = array[0]
        end = (begin + BLOCK_SIZE)
        print begin,end
        if begin >= FILE_SIZE:
            print 'begin:',begin
            array[0] = begin
            raise Exception('end of file')
        elif end < FILE_SIZE:
            fs.seek(end)
            #  read one more line to ensure contents of file are read     
            fs.readline()
            end = fs.tell()
        elif end >= FILE_SIZE:
            end = FILE_SIZE
        
        array[0] = end
        print '===================', begin, end
        
    except Exception,e:
        print e.__class__.__name__,str(e)   
        return
    
    finally:
        rclock.release()
        
    fs.seek(begin)
    pos = begin
    
    fd = open('/home/yang/Test/'+str(pid)+'_jobs','wb')
    
    while pos < end:
        fd.write(fs.readline())
        pos = fs.tell()
        
    fs.close()
    fd.close()

def main():
    global FILE_SIZE,BLOCK_SIZE,WORKERS,FILE_NAME
    
    getFileSize(FILE_NAME)
    
    BLOCK_SIZE = FILE_SIZE/WORKERS
    
    print 'The Size of File: %d and the Block Size: %d' % (FILE_SIZE,BLOCK_SIZE)
    
    rclock = mp.RLock()
    array = mp.Array('l',WORKERS)
    array[0] = 0 
    
    processes = [mp.Process(target=process,args=[i,array,rclock]) for i in xrange(WORKERS)]
    
    for i in xrange(WORKERS):
        processes[i].start()
        
    for i in xrange(WORKERS):
        processes[i].join()
              
if __name__ == '__main__':
   
    start = time.time()
    
    main()
    

    
    end = time.time() - start
    
    print "Total Running Time: %f"  % end