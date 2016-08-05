#!/usr/bin/python2
import os,commands,socket,time
os.system('dialog --infobox "NFS server is ready to create" 10 30')
time.sleep(2)
os.system('rpm -q nfs-utils')
time.sleep(2)
os.system('yum install nfs-utils')
time.sleep(2)
os.system('systemctl enable nfs')
time.sleep(1)
os.system('systemctl restart nfs')
time.sleep(1)
os.system('systemctl status nfs')
time.sleep(2)
os.system('exportfs -r')


