#!/usr/bin/python3

#Copyright 2013-2016, eehp <fel.putinier@gmail.com>
#
# This file is part of Raclette.
# 
# Raclette is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Raclette is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Raclette.  If not, see <http://www.gnu.org/licenses/>.
#


import sys
import os

## Variables ##

exit = 0
option = ["-O","-sS", "-sU"]
get_gateway = "sysnet -n | grep Gateway | cut -f 2 -d:"
get_suffix = "sysnet -n | grep suffix | tail -n 1 | cut -f 3 -d:"
get_ipaddress = "sysnet -n | grep address | tail -n 3 |cut -f 2 -d:  "
Outgate = os.popen(get_gateway).readlines()
str_gateway = Outgate[0]
Outsuffix =  os.popen(get_suffix).readlines()
str_suffix = Outsuffix[0]
OutIpAddress = os.popen(get_ipaddress).readlines()
str_IP = OutIpAddress[0]
exit1 = 0
File = 0

## Variables ##

def swag_logo():
	print("                _      _   _       ")
	print(" _ __ __ _  ___| | ___| |_| |_ ___ ")
	print("| '__/ _` |/ __| |/ _ \ __| __/ _ \ ")
	print("| | | (_| | (__| |  __/ |_| ||  __/   ")
	print("|_|  \__,_|\___|_|\___|\__|\__\___|\n")

def check4root(): # This function checks if you User ID is 0, if not, you're not root :(
	uid = os.getuid() 
	if (uid != 0):
		print ("Please, run this script as root")
		sys.exit()

check4root()
swag_logo()


while (exit1 == 0): # Choose between your machine & Your subnetwork.
	exit1 = exit1 + 1
	target = int(input ("1) Your Machine\n2) Subnetwork\n> "))
	
	if (target == 1 ): # You have choose your machine.
		target = str_IP
		os.system("clear")
		swag_logo()

		while True: # Choose between OS TCP and UDP Scans.
			print ("1) OS detection\n2) Scans TCP SYN ports\n3) Scans UDP ports")
			option_1 = int(input("> "))
			
			if (option_1 == 1 or option_1 == 2 or option_1 == 3) :
				break
			
			else:
				print ("[!] Enter a valid number\n")
	
	elif (target == 2 ): # You have choose your Subnetwork.
		target = str_gateway[:13] + "/" + str_suffix[1:]
		print (target)
		
		while True: # Choose between OS TCP and UDP Scans.
			print ("1) OS detection\n2) Scans TCP SYN ports\n3) Scans UDP ports")
			option_1 = int(input("> "))
			
			if (option_1 == 1 or option_1 == 2 or option_1 == 3):
				break
			
			else:
				print ("[!] Enter a valid number\n")
	
	else: 
		print ("[!] Enter a valid number\n")
		exit1 = 0


if (option_1 == 1): # You have choose OS scan. Now you can choose a second option.
	option_2 = input("[?] Choose another option ? [Y/n]: ")
	option_2 = option_2.lower()
	
	if option_2 == "y" or option_2 == "":
		
		while True: # Choose between TCP and UDP for the second option.
			os.system("clear")
			swag_logo()
			choix_option_2 = input("1) Scans TCP SYN ports\n2) Scans UDP ports\n")
			
			if (choix_option_2 == "1"): 
				option_3 = input("[?] Choose another option ? [Y/n]: ") # You can choose a third option.
				option_3 = option_3.lower()
				
				if option_3 == "y" or option_3 == "": # You will make a OS TCP and TCP scans.
					print ("Raclette do ",option[0] + " " + option[1] + " " + option[2], " Scan on " + target)
					print ("It may take a while...\nTake a seat and have a break\n")
					os.system("nmap" + " " + option[0] + " " + option[1] + " " + option[2] + " " + target)
				
				else: # You will make a OS and TCP scans.
					print ("Raclette do ",option[0] + " " + option[1], " Scan on " + target)
					print ("It may take a while...\nTake a seat and have a break\n")
					os.system("nmap" + " " + option[0] + " " + option[1] + " " + target)
					break
			
			elif (choix_option_2 == "2"):
				option_3 = input("[?] Choose another option ? [Y/n]: ") # You can choose a third option.
				option_3 = option_3.lower()
				
				if option_3 == "y" or option_3 == "": # You will make a OS TCP and TCP scans.
					print ("Raclette do ",option[0] + " " + option[1] + " " + option[2], " Scan on " + target)
					print ("It may take a while...\nTake a seat and have a break\n")
					os.system("nmap" + " " + option[0] + " " + option[1] + " " + option[2] + " " + target)
					break
				
				else: # You will make a OS and UDP scans.
					print ("Raclette do ",option[0] + " " + option[2], " Scan on " + target)
					print ("It may take a while...\nTake a seat and have a break\n")
					os.system("nmap" + " " + option[0] + " " + option[2] + " " + target)
					break
			
			else:
				print ("[!] Enter a valid number")
	
	else: # You will make a OS scans.
		print ("Raclette do ",option[0], " Scan on " + target)
		print ("It may take a while...\nTake a seat and have a break\n")
		os.system("nmap" + " " + option[0] + " " + target)

elif (option_1 == 2): # You have choose TCP scan. Now you can choose a second option.
	option_2 =input("[?] Choose another option ? [Y/n]: ")
	option_2 = option_2.lower()
	
	if option_2 == "y" or option_2 == "":
		
		while True: # Choose between OS and UDP Scans.
			os.system("clear")
			swag_logo()
			choix_option_2 = input("1) OS detection\n2) Scans UDP ports\n> ")
			
			if (choix_option_2 == "1"):
				option_3 = input("[?] Choose another option ? [Y/n]: ") # You can choose a third option.
				option_3 = option_3.lower()
				
				if option_3 == "y" or option_3 == "": # You will make a OS TCP and TCP scans.
					print ("Raclette do ",option[0] + " " + option[1] + " " + option[2], " Scan on " + target)
					print ("It may take a while...\nTake a seat and have a break\n")
					os.system("nmap" + " " + option[0] + " " + option[1] + " " + option[2] + " " + target)
					break
				
				else: # You will make a OS and TCP scans.
					print ("Raclette do ",option[0] + " " + option[1], " Scan on " + target)
					print ("It may take a while...\nTake a seat and have a break\n")
					os.system("nmap" + " " + option[0] + " " + option[1] + " " + target)
					break
			
			elif (choix_option_2 == "2"):
				option_3 = input("[?] Choose another option ? [Y/n]: ") # You can choose a third option.
				option_3 = option_3.lower()
				
				if option_3 == "y" or option_3 == "": # You will make a OS TCP and TCP scans.
					print ("Raclette do ",option[0] + " " + option[1] + " " + option[2], " Scan on " + target)
					print ("It may take a while...\nTake a seat and have a break\n")
					os.system("nmap" + " " + option[0] + " " + option[1] + " " + option[2] + " " + target)
					break
				
				else:# You will make a UDP and TCP scans.
					print ("Raclette do ",option[1] + " " + option[2], " Scan on " + target)
					print ("It may take a while...\nTake a seat and have a break\n")
					os.system("nmap" + " " +  option[1] + " " + option[2] + " " + target)
					break
			
			else:
				print ("[!] Enter a valid number")
	
	else: # You will make a TCP scans.
		print ("Raclette do ",option[1], " Scan on " + target)
		print ("It may take a while...\nTake a seat and have a break\n")
		os.system("nmap" + " " +  option[1] + " " + target)


elif (option_1 == 3): # You have choose UDP scan. Now you can choose a second option.
	option_2 =input("[?] Choose another option ? [Y/n]: ")
	option_2 = option_2.lower()
	
	if option_2 == "y" or option_2 == "":
		
		while True: # Choose between OS and TCP Scans.
			os.system("clear")
			swag_logo()
			choix_option_2 = input("1) OS detection\n2) Scans TCP SYN ports\n> ")
			
			if (choix_option_2 == "1"):
				option_3 = input("[?] Choose another option ? [Y/n]: ") # You can choose a third option.
				option_3 = option_3.lower()
				
				if option_3 == "y" or option_3 == "": # You will make a OS TCP and TCP scans.
					print ("Raclette do ",option[0] + " " + option[1] + " " + option[2], " Scan on " + target)
					print ("It may take a while...\nTake a seat and have a break\n")
					os.system("nmap" + " " + option[0] + " " + option[1] + " " + option[2] + " " + target)
				
				else:# You will make a UDP and OS scans.
					print ("Raclette do ",option[0]+ " " + option[2], " Scan on " + target)
					print ("It may take a while...\nTake a seat and have a break\n")
					os.system("nmap" + " " + option[0] + " " + option[2] + " " + target)
					
			
			elif (choix_option_2 == "2"):
				option_3 = input("[?] Choose another option ? [Y/n]: ") # You can choose a third option.
				option_3 = option_3.lower()
				
				if option_3 == "y" or option_3 == "": # You will make a OS TCP and TCP scans.
					print ("Raclette do ",option[0] + " " + option[1] + " " + option[2], " Scan on " + target)
					print ("It may take a while...\nTake a seat and have a break\n")
					os.system("nmap" + " " + option[0] + " " + option[1] + " " + option[2] + " " + target)
				
				else: # You will make a UDP and TCP scans.
					print ("Raclette do ",option[1] + " " + option[2], " Scan on " + target)
					print ("May take a while...\nTake a seat and have a break\n")
					os.system("nmap" + " " +  option[1] + " " + option[2] + " " + target)
			
			else:
				print ("[!] Enter a valid number")
	
	else: # You will make a UDP scans.
		print ("Raclette do ",option[2], " Scan on " + target)
		print ("It may take a while...\nTake a seat and have a break\n")
		os.system("nmap" + " " + option[2] + " " + target)

else:
	print ("[!] Enter a valid number")
print ("[I] RACLETTE stopped.")
