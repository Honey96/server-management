#!/usr/bin/python2
import os,getpass,time,commands,socket
os.system('tput setaf 1 ')
os.system('dialog --infobox "welcome to my tools for server management" 10 30')
time.sleep(2)
while True:
	os.system(' dialog --menu "select one" 10 50 7  1 "Apache server" 2 "Ftp server" 3 "Ssh server" 4 "Nfs server" 5 "Samba server" 6  "Telnet server" 7 "nisserver" 8 "exit" 2>/root/Desktop/project1/ch.txt')
	aout1=open('/root/Desktop/project1/ch.txt')
	choice=aout1.read()
	aout1.close()
	if choice == '1':
		import apacheserver
	elif choice == '2':
		import ftpserver
	elif choice == '3':
		import sshserver
	elif choice == '4':
		import nfsserver
	elif choice == '5':
		import sambaserver
	elif choice == '6':
		import telnetserver
        elif choice == '7':
		import nisserver
	elif choice == '8':
		os.system('dialog --infobox "Exiting from the project" 10 30')
		time.sleep(2)
		exit() 
	


