#!/usr/bin/python2                                                              
import os,time,commands,socket,getpass
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
os.system('dialog --infobox "\tWelcome to my project\n Hope you will find it interesting" 10 50')
time.sleep(2)
os.system(' dialog --menu "select one" 10 50 2  1 "Enter into my Project" 2 "Exit"  2>/tmp/ch.txt ')
lout1=open('/tmp/ch.txt')
choice=lout1.read()
s.sendto(choice,("192.168.0.6",1234))
lout1.close()
usr="harshit"
psd="redhat"
if choice == '1':
	os.system("dialog --inputbox 'Enter the name of the Admin' 10 30 2>  /root/Desktop/project/admin.txt")
        lout2=open('/root/Desktop/project/admin.txt','r')
        u=lout2.read()
	s.sendto(u,("192.168.0.6",1234))
        lout2.close   
	os.system("dialog --inputbox 'Enter the password of the project' 10 30 2>  /root/Desktop/project/password.txt")
        lout2=open('/root/Desktop/project/password.txt','r')
        p=lout2.read()
	s.sendto(p,("192.168.0.6",1234))
        lout2.close 
        os.system('dialog --infobox "Checking details.." 10 30')
	time.sleep(2)
        if usr ==u  and psd==p:
                        os.system('dialog --infobox "\tBravo! Successfully entered" 10 30')
			
	else:
			os.system('dialog --infobox "/tSorry details are incorrect../nTry next time" 10 30')
elif choice == '2':
		os.system('dialog --infobox "Thank you for logging into the project" 10 30')
		time.sleep(2)
		os.system('clear')




