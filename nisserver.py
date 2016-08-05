#!/usr/bin/python2
import os,commands,socket,time
os.system('dialog --infobox "Nis server is ready to create" 10 30')
time.sleep(2)
os.system('rpm -q ypserv')
time.sleep(2)
os.system("dialog --inputbox 'Enter the name of the domain' 10 30 2>  /root/Desktop/project1/fentry.txt")
tfout=open('/root/Desktop/project1/fentry.txt','r')
tel1=tfout.read()
tfout.close
os.system('nisdomainname '+tel1)
time.sleep(2)
os.system('systemctl restart ypserv')
os.system('systemctl enable ypserv')
os.system('cd /var/yp/')
os.system('make')
os.system("dialog --inputbox 'Enter the name of the user' 10 30 2>  /root/Desktop/project1/userentry.txt")
tfout=open('/root/Desktop/project1/userentry.txt','r')
tel2=tfout.read()
tfout.close
os.system('useradd  -u 5000 '+tel2)
os.system('passwd '+tel2)
os.system('make')
os.system('dialog --infobox "nis server is  created" 10 30')
time.sleep(2)


