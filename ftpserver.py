#!/usr/bin/python2
import os,commands,time,socket
def ftp1():
	os.system('dialog --infobox "ftp is ready to create" 10 30')
        time.sleep(2)  
	os.system('rpm -q vsftpd')
	time.sleep(2)       
	os.system('systemctl restart vsftpd')
	time.sleep(2)
	os.system('systemctl status vsftpd')   
	time.sleep(2) 
	os.system('systemctl enable  vsftpd')      
	os.system('dialog --infobox "ftp is successfully created" 10 30')
        time.sleep(2)

ftp1()
       		              
	
