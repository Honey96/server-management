#!/usr/bin/python2
import os,commands,socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.0.5",9997))
for num in range(0,3):
	x=s.recvfrom(1000)
	print x
os.system('dialog --infobox "Telnet client is ready to create" 10 30')
time.sleep(2)
os.system('rpm -q telnet')
time.sleep(2)
os.system('yum install telnet')
os.system("dialog --inputbox 'Enter the server ip' 10 30 2>  /root/Desktop/project1/fentry.txt")
tfout2=open('/root/Desktop/project1/fentry.txt','r')
tel3=tfout2.read()
tfout2.close
os.system('telnet '+tel3)

