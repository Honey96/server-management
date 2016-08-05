#!/usr/bin/python2
import os,commands,socket,time
os.system('dialog --infobox "NFS client is ready to create" 10 30')
time.sleep(2)
os.system("dialog --inputbox 'Enter the server ip or hostname' 10 30 2>  /root/Desktop/project1/fentry.txt")
nfout=open('/root/Desktop/project1/fentry.txt','r')
nfs1=nfout.read()
nfout.close
os.system('showmount -e  '+nfs1)
os.system("dialog --inputbox 'Enter the name of the directory you want to share' 10 30 2>  /root/Desktop/project1/direc.txt")
os.system('dialog --infobox "Shared folder will be in default media location" 10 30')
nfout=open('/root/Desktop/project1/direc.txt','r')
nfs2=nfout.read()
nfout.close
os.system('mkdir /media/'+nfs2)
time.sleep(2)
os.system('dialog --infobox "Ready for mounting" 10 30')
time.sleep(2)
os.system('mount -t nfs '+nfs1+':/media /'+nfs2)
os.system('dialog --infobox "Successfully mounted check in media " 10 30')
time.sleep(2)



