#!/usr/bin/python2
import os,commands,socket,time
os.system('dialog --infobox "Ssh server is ready to create" 10 30')
time.sleep(2)
os.system('rpm -q openssh-server')
time.sleep(2)
os.system('systemctl restart sshd')
time.sleep(2)
os.system('systemctl status sshd')
time.sleep(2)
os.system('systemctl enable sshd')
os.system('dialog --infobox "SSH SERVER is successfully created" 10 30')
time.sleep(2)


