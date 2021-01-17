
import os
import datetime

path = "Users\shiva\OneDrive\Desktop\projects"
directory = os.path.join("c:\\", path)
data = ""
for root,dirs,files in os.walk(directory):
    for file in files:
        if file.endswith(".log"):
            with open(file, 'rU') as f:
                data = data + f.read() + "\n"
            f.close()
           
ts = str(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
extension = ".txt"
file_name =  ts + extension
file = open(file_name, 'w')
file.write(data)
file.close()
             
             
             
             
             
             
             
