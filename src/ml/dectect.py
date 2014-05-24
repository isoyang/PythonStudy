# Uesage Terminal: python detect.py  -l file  -r regular expression

# python detect.py -l file  to generate the most 5 common words in file 

# example python detect -l /home/usr/file

# python detect.py -l file -r regular expression to generate the words filtered by regular expression and its number of occurrence

# exaple  python detect.py -l /home/usr/file.txt -r ^H.*  

import string,re,sys,os,getopt

# add word into the word dictionary. word_dict is used for storing the words and its number of occurrence.
def add_word(word,word_dict):
    
    if word in word_dict:
        
        word_dict[word] += 1
    else:
        
        word_dict[word] =1  

# trim the string line by line including punctuation, except for emoticon 
def process_line(line,reg,word_dict):
    
    emoticon_pattern = re.compile(reg,re.I)

    word_list = line.strip().split(" ")

    for index,word in enumerate(word_list):
        
        m = emoticon_pattern.search(word) 
         
        if not m:
                        
            word = word.strip(string.punctuation)
            
        add_word(word,word_dict)

# calculate the statistics of words in the file       
def calfreq(word_dict,**arg):
    
    val_key_list = []
        
    if not arg:
        
        for key,val in word_dict.iteritems():
             
            val_key_list.append((val,key)) 
            
    else:
        
        para_list = []
        
        for key in arg.keys():
            
            para_list.append(str(arg[key]))
            
        p = re.compile(para_list[0],re.I)
        
        for key,val in word_dict.iteritems():
            
            if p.search(key):
                
                val_key_list.append((val,key))
                     
    val_key_list.sort(reverse=True)
    
    return val_key_list

# print word
def print_result(val_key_list,number):
   
    for val,key in val_key_list[:number]:
        
        print "%-12s   %3d" %(key,val)    

#help message       
def useage():
    
    print """ 
    
    Try to segment the files and calculate the frequency of words happening in the file.
    
    -f  indicate the location of file 
    
    -r specify the regular expression like r'......'
        
    """  
    sys.exit(1)

# judge whether it represents a file or directory  
def warningFile():

    
    print """ 
    
    File does not exit, or  address you specified is a directory.
    
    Please enter an existing file address
    
    """
    sys.exit(1)

# judge wehether the file is empty
def warningEmpty():
   
    print """ 
    
    Your specified File is identified as empty file. Please Try another File
    
    """
    
    sys.exit(1)

# judge wheter the path exits in current system 
def warningPath():
    
    print """ 
    
    Your specified Path does not exit
    
    Please choose another path for input!!!
    
    """
    sys.exit(1)    

def warningOut():
    
    print """
    
    The Number you specified has been out of range of word list!!!!
    
    """
    sys.exit(1)
    
if __name__ == '__main__':    
    # accept parameters from command line    
    try:
        
        opts = getopt.getopt(sys.argv[1:], "l:r:h")[0]
    except getopt.GetoptError:
        
        useage()
    
    try:
        indicator = False
        for opt,val in opts:
            
            # file location 
            if opt == "-l":
                
                param = val
                
                if os.path.exists(param):
                    
                    if not os.path.isfile(param):
                        
                        warningFile()
                        
                    else:
                        
                        if os.stat(param).st_size == 0:
                            
                            warningEmpty()                              
                else:
                    
                    warningPath()
            # regular expression is specified for filerting certain words in the file                       
            elif opt == "-r":
                
                indicator = True
                
                reg = val
            # help option                  
            elif opt == "-h":
                
                useage()
                
        word_dict={}
    
        # match emoticon text code
        # smile: :) =) :-) :D :-D :} :] :^)
        # Sad:   :( :-( =(
        #Crying: :'(
        #Stick that tongue: :p :P :-p :-P
        #shocked: :o 
        # angry: :@
        #Confused:  :s :S
        #Wink: ;) ;-)
        # Embarrassed: :$
        #Disappointed: :|
        # Sick:  +o(
        #Shut Mouth :-#
        #Sleepy: |-)
        #eyeroll: 8-)
        #thinking :\ *-) :-\
        #Yes: (Y) No: (No)
        #love heart (L)
        #broken heart (U)
        #coffee (C)
        #present (G)
        #cake (^)
        emoticon_re = r'^\(?[\^gcuyndl8\|+\':;=*>]?[-o\^\):\.]?[<\(\)pdos@\|\$\#\\\]\}]?$'
        
        # read data from file 
        data = open(param,'rb')
        
        # process data line by line
        for line in data.readlines():
        
            process_line(line,emoticon_re,word_dict)
            
        # judge whether show 5 most common words in the file or customized words selection by regular expression.  
        if indicator:
            
            filtered_list = calfreq(word_dict,re=reg)
            print_result(filtered_list,len(filtered_list))
                        
        else:    
            
            val_key_list = calfreq(word_dict)        
            
            if len(val_key_list) > 5:
                
                print_result(val_key_list,5)
            else:
                
                warningOut()
        
    except getopt.GetoptError:
        
        print 'Please check whether your input is a real file address'
   


