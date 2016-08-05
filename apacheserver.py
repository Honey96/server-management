#!/usr/bin/python2
import os,commands,socket,time
os.system('dialog --infobox "Apache is ready to create" 10 30')
time.sleep(2)
os.system('rpm -q httpd')
time.sleep(2)
os.system('systemctl restart httpd')
time.sleep(2)
os.system('systemctl status httpd')
time.sleep(2)
os.system('systemctl enable httpd')
os.system('dialog --infobox "Apache server is Successfully created" 10 30')



