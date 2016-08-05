#!/usr/bin/python2
import os,commands,socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
os.system('dialog --infobox "Telnet server is ready to create" 10 30')
time.sleep(2)
os.system('rpm -q telnet-server')
time.sleep(2)
os.system('yum install telnet-server')
time.sleep(2)
os.system('systemctl restart telnet.socket')
os.system('systemctl status telnet.socket')
time.sleep(2)
s.sendto("login details",("192.168.0.5",9997))
time.sleep(2)
os.system("dialog --inputbox 'Enter the name of the user' 10 30 2>  /root/Desktop/project1/fentry.txt")
tfout=open('/root/Desktop/project1/fentry.txt','r')
tel1=tfout.read()
s.sendto("username is"+tel1,("192.168.0.5",9997))
tfout.close
os.system("dialog --inputbox 'Enter the password of the user' 10 30 2>  /root/Desktop/project1/passwd.txt")
tfout=open('/root/Desktop/project1/passwd.txt','r')
tel2=tfout.read()
s.sendto("password is"+tel2,("192.168.0.5",9997))
tfout.close
os.system('dialog --infobox "Waiting for Password " 10 30')
time.sleep(2)
os.system('useradd '+tel1)
os.system('passwd '+tel1)




