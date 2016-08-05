#!/usr/bin/python2
import os,commands,time,socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
os.system("dialog --inputbox 'Enter the ip address of the system' 10 30 2>  /root/Desktop/project1/fentry.txt")
tfout=open('/root/Desktop/project1/fentry.txt','r')
smb1=tfout.read()
tfout.close
s.sendto("ip address of the server is ",(smb1,9996))
os.system('dialog --infobox "Samba server is ready to create" 10 30')
time.sleep(2)      
os.system('rpm -q samba')
time.sleep(2)
os.system('systemctl restart smb')
os.system('systemctl enable smb')
os.system('dialog --infobox "Samba server is Created successfully" 10 30')




































































































































