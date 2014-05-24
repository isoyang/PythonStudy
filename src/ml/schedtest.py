## Usage  Terminal: python status.py url time_interval 

import time, sys, sched, pycurl, argparse, re
 
# calass TestSize is used for calculating the size of the data fetched from the target web.  
class TestSize():
    
    def __init__(self):
        self.content= ""
     
    # calculate the size   
    def body_callback(self,buf):
        self.content = self.content + buf

# get the status information of request by using library pycurl      
def calurl(url):
    
    t = TestSize()
    
    c = pycurl.Curl()
    
    # settings
    c.setopt(pycurl.WRITEFUNCTION,t.body_callback)
    c.setopt(pycurl.CONNECTTIMEOUT,30)
    c.setopt(pycurl.TIMEOUT,60)
    c.setopt(pycurl.ENCODING,'gzip')
    c.setopt(pycurl.MAXREDIRS, 5)
    c.setopt(pycurl.USERAGENT, "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)")
    c.setopt(pycurl.URL,url)
    
    try:
        # fetch the data
        c.perform()
    
        http_code = c.getinfo(pycurl.HTTP_CODE)
        http_con_time = c.getinfo(pycurl.CONNECT_TIME)
        http_pre_tran = c.getinfo(pycurl.PRETRANSFER_TIME)
        http_start_tran =  c.getinfo(pycurl.STARTTRANSFER_TIME)
        http_total_time = c.getinfo(pycurl.TOTAL_TIME)
        http_size = c.getinfo(pycurl.SIZE_DOWNLOAD)
    
    except pycurl.error:
        
        http_code = -1
    
    print 'The information of target website is as follows:' 
    print '################################################'  
    print '\tStatus: %s' % http_code
    print '\tSize: %d Byte(s)' % http_size
    print '\tConnection Time: %10.4f second(s)' % http_con_time
    print '\tPreTransfer Time: %10.4f second(s)' % http_pre_tran
    print '\tStarttransfer Time: %10.4f second(s)' % http_start_tran
    print '\tTotal Time: %10.4f second(s)' % http_total_time
    print '################################################'
    print ''
    
# let the program running periodically via Library Sched
schedule = sched.scheduler(time.time, time.sleep) 

# let the program call itself every inc seconds  
def perform_command(cmd,inc): 
   
    schedule.enter(inc, 0, perform_command, (cmd,inc)) 
    
    calurl(cmd)

 
# initialize the program     
def time_exe(cmd,inc): 
    
    schedule.enter(0, 0, perform_command, (cmd,inc))     
    schedule.run() 

# accept the parameters from command line
# both url and time interval  will be fetched from input     
def mymain(argv):
    
    parser = argparse.ArgumentParser(description='URL request time periodically')
    
    parser.add_argument('URL',help='requested URL')
    
    parser.add_argument('Time',type=int,help='time interval')
    
    args = parser.parse_args(argv)
    
    url = args.URL
    nmt = args.Time
    
    if re.match(r'^https?:/{2}\w.+$',url):
          
        time_exe(url,nmt)
    
if __name__ == '__main__':
    
    mymain(sys.argv[1:])