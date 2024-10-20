# these are imports it imports external library like colorama or internal like os sys and time
# to install colorama youll need to open a shell and write the following command 
# by the way colorama is used to produce color in a python shell like color commands in cmd
import os 
import colorama
import sys
from colorama import Fore
import time

# this is the command to add color, write Fore. and then add the name of your color, you can find all the color name on colorama page

# this is the menu function 
#it'll make the shell interface using a print and then you can paste any ascii text to make an interface

def menu():
	global onstart
	print(f"""





				 
{Fore.MAGENTA}████████╗███████╗███████╗████████╗
{Fore.WHITE}╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
{Fore.MAGENTA}   ██║   █████╗  ███████╗   ██║   
{Fore.WHITE}   ██║   ██╔══╝  ╚════██║   ██║   
{Fore.MAGENTA}   ██║   ███████╗███████║   ██║   
{Fore.WHITE}   ╚═╝   ╚══════╝╚══════╝   ╚═╝   
                                  

{Fore.MAGENTA}                                                                                                   
[help]	[shutdown]

[0] Exit              [3] Random Cmd #3
[1] Random Cmd #1     [4] Random Cmd #4
[2] Random Cmd #2     [5] Random Cmd #5

{Fore.WHITE}
""")

# this is the command variable, its an input() btw between these () after the input you can writ everything you want im gonna show this to you

	command = input(">")

	
#this is the command pattern 
# i coded the exit command to help you with atleast one command

	if command == "5":
		print("command")

	if command == "0":
		print("> Do you really want to leave ?")
		command = input("> Y/N $>")
		time.sleep(1)

	if command == "2":
		print("command")

	if command == "3":
		print("command")

	if command == "4":
		print("command")

	if command == "Y":
		time.sleep(1)
		print("> Exiting.. See you next time !")
		time.sleep(1)
		sys.exit(0)

	if command == "N":
		time.sleep(1)
		print("> Nevermind.. You're Back !")
		time.sleep(1)
		onstart()

	if command == "help":
		time.sleep(1)
		print("""> Contact :
		
			Discord ID : XXXXXXXXXXXXXXXXXX
			Github : intel1337

		""")
		time.sleep(1)
		onstart()

	if command == "1":
		print("command")

	if command == "shutdown":
		sys.exit()

def onstart():
    cmd = 'mode 120,28' # this define the size of your shell window
    os.system(cmd) # this will execute the variable associated to the size in the shell
    os.system("cls && title Test - Multitool")# this will clear the commands written and all the prints after the command has executed
    menu() # this add the menu "gui"

onstart()



 