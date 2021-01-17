import os
import datetime

file_number = 0
file_size = 0
 
while True:
    ts = datetime.datetime.now()
    #2e+6 equals 2Mb
    if file_size <= 2e+6:
        try:
            file = open('file%d.log'%file_number, 'x')
            
        except:
            pass 
        f = open('ex.log','r')
        log = f.read()
        file = open('file%d.log'%file_number)
        text = file.read() + str(ts)+ log
        file = open('file%d.log'%file_number, 'w')
        file.write(text)
        file.write("\n")
        file.write("\n")
       
    file_size = os.stat('file%d.log'%file_number) .st_size
    if file_size > 2e+6:
        file_number += 1
        file_size = 0