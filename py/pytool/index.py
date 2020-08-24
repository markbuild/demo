#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author Mark Li(https://github.com/markbuild)
# Function:Mark Li's Python Toolkit
# MPID:67
import colorprint
from externalip import externalip # Get external IP of your computer
from scanmyport import scanmyport # Scan some important port
from synchronize import synchronize #Synchronnize files to removable disk
from zipbackup import zipbackup
from createhtml5 import createhtml5 #Create a basic HTML5 template file
from md5sha import md5sha # .exe MD5、SHA-1、SHA-256、SHA-512
from countdokupages import countdokupages # .exe MD5、SHA-1、SHA-256、SHA-512
from synmusic import synmusic #Synchronnize files to removable disk
import re

def main():
    logo ="""
                           _                _     
            ____  _   _ __| |__ ____  ____ | |   
           /  _ \| | | |\_   _//  _ \/  _ \| |  
           | |_| | |_| |  | |_.| |_| | |_| | |__.
           | ___/ \__. |  \___/ \___/ \___/\____/
           |_|    |___/
"""
    colorprint.color_print(logo,'pink')
    colorprint.color_print("         --- Mark's Python toolkit since 2015 --- \n",'skyblue')
    menu ='-'*60+'\n'+"""
[1] externalip: Get external IP of your computer
[2] scanmyport: Scan some important port of your computer
[3] synchronize: Synchronnize files to removable disk
[4] zipbackup: Zip Backup
[5] createhtml5: Create a basic HTML5 template file
[6] md5sha: .exe MD5、SHA-1、SHA-256、SHA-512
[7] countdokupages: count doku pages
[8] synmusic: Synchronnize music files to SD card 
[x] exit: Exit
"""+'\n'+'-'*60

    colorprint.color_print(menu,'yellow')
    while True:
        command = input(">>")
        if command=="exit" or command=="x":
            colorprint.color_print('Byebye!','pink')
            break
        elif command=="h":
            colorprint.color_print(menu,'yellow')
        else:
            process_command(command)

def process_command(cmd):
    try:
        if len(re.findall(r'^\d+$',cmd))>0:
            eval('c'+cmd)()
        else:
            eval(cmd)()
    except:
        colorprint.color_print('Wrong command','red')

c1 = externalip #Point to the same memory address
c2 = scanmyport
c3 = synchronize
c4 = zipbackup
c5 = createhtml5 
c6 = md5sha 
c7 = countdokupages 
c8 = synmusic 
main()
            


