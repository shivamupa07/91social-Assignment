import os
import subprocess

#ping and check whether any given IPs are active
with open(os.devnull, "wb") as limbo:
    ip=input("Enter ip Address: ")
    ip = ip.replace(" ","")
    ip_list = ip.split(",")
    for i in range(len(ip_list)):
        result=subprocess.Popen(["ping", "-n", "1", "-w", "200", ip_list[i]],
        stdout=limbo, stderr=limbo).wait()
        if result:
            print(ip_list[i], "inactive")
        else:
            print(ip_list[i], "active")

#check whether any given set of software are installed in the system
print("\n")
sftware_name = input("Enter software name: ")
sftware_name = ",".join(sftware_name.split(", "))
sftware_list = sftware_name.split(",")
data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
a = str(data) 
lst = []

try: 
    
    for i in range(len(a)):
        st = a.split("\\r\\r\\n")[6:][i]
        st = " ".join(st.split())
        lst.append(str(st))
    
except IndexError as e:
    for software in sftware_list:
        for i in range(len(lst)):
            if software.lower() in lst[i].lower():
                print(software+": Is installed")
                break
            elif i == len(lst)-1:
                print(software+": Is not installed")
                break
            else:
                pass
            