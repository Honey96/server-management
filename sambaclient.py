#!/usr/bin/python2
import os,commands,socket,time
os.system('rpm -q cifs-utils')
time.sleep(2)
os.system("dialog --inputbox 'Enter the ip address of the system' 10 30 2>  /root/Desktop/project1/fentry.txt")
tfout=open('/root/Desktop/project1/fentry.txt','r')
smb2=tfout.read()
tfout.close
os.system('smbclient -U me //'+smb2+'/sharename')
os.system('dialog --infobox "Samba client is Created successfully" 10 30')
