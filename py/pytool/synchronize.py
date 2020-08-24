#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author Mark Li(https://github.com/markbuild)
# Function: Synchronnize files to removable disk

import os
import shutil
import re
import time
import colorprint

from ctypes import windll
import string

def synchronize():
    avaiabel_drives=_getDrives()
    avaiabel_drives_lens = len(avaiabel_drives)
    if avaiabel_drives_lens == 1:
        removable_disk_volume = avaiabel_drives[0]
    elif avaiabel_drives_lens == 0:
        colorprint.color_print('Please connect the data cable and retry!','red')
        return
    else:
        colorprint.color_print('Please choose the volume serial number of your removable disk:(Current avaiable drives:'+','.join(avaiabel_drives)+')','yellow')
        removable_disk_volume = input(">>")

    backdirs=[['C:\\Users\\Mark\\OneDrive\\music',removable_disk_volume+':\\backup\\music'],
	      ['C:\\markli\\tool',removable_disk_volume+':\\backup\\tool']
            ]
    for backdir in backdirs:
        if not os.path.exists(backdir[1]):
            os.makedirs(backdir[1])
        _clearbackup(backdir[0],backdir[1])
        _syncbackup(backdir[0],backdir[1])

    colorprint.color_print('Synchronnize completed!','pink')

#Synchronnize to backup
def _syncbackup(ori_dir,aim_dir):
    os.chdir(ori_dir) # Changes the current working directory to orginal directory 
    listdir = os.listdir()
    for name in listdir: # Directory traversal 
        if len(re.findall(r'\.swo$',name))>0 or len(re.findall(r'\.swp$',name))>0 or len(re.findall(r'~$',name))>0 or name =='Thumbs.db':
            continue
        if os.path.isfile(ori_dir+'\\'+name):# If file 
            if not os.path.exists(aim_dir+'\\'+name):# If backup repository don't have this file
                shutil.copy2(ori_dir+'\\'+name, aim_dir+'\\'+name) #  Backup this file 
                colorprint.color_print('Backup repository added new file：' + aim_dir+'\\'+name,'skyblue')
            elif os.path.getmtime(ori_dir+'\\'+name) != os.path.getmtime(aim_dir+'\\'+name):# If the modified date of this file are not the same than aim file
                shutil.copy2(ori_dir+'\\'+name, aim_dir+'\\'+name) # update this file
                colorprint.color_print('Backup repository updated file：' + aim_dir+'\\'+name,'yellow')
        elif os.path.isdir(ori_dir+'\\'+name):# If directory
            if not os.path.exists(aim_dir+'\\'+name):# If backup repository don't have this directory
                os.makedirs(aim_dir+'\\'+name) # Create this directory
                colorprint.color_print('Backup repository added new directory：'+aim_dir+'\\'+name,'pink')
            _syncbackup(ori_dir+'\\'+name,aim_dir+'\\'+name) # Recursion/递归

# Remove the file which already removed from origin repository 
def _clearbackup(ori_dir,aim_dir):
    os.chdir(aim_dir)# Changes the current working directory to aim directory
    listdir = os.listdir()
    for name in listdir:# Directory traversal
        if os.path.isfile(aim_dir+'\\'+name): # If file
            if not os.path.exists(ori_dir+'\\'+name): # If the file not exsit on origin repository 
                os.remove(aim_dir+'\\'+name) # Remove this file
                colorprint.color_print('Backup repository deleted file：' + aim_dir+'\\'+name,'red')
        elif os.path.isdir(aim_dir+'\\'+name):# If directory
            if not os.path.exists(ori_dir+'\\'+name):# If this directory not exsit on origin repository
                shutil.rmtree(aim_dir+'\\'+name) # Remove this directory
                colorprint.color_print('Backup repository deleted directory：'+aim_dir+'\\'+name,'red')
            else:
                _clearbackup(ori_dir+'\\'+name,aim_dir+'\\'+name) # Recursion/递归

def _getDrives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_lowercase:
        if bitmask & 1 and letter !='c':
            drives.append(letter)
        bitmask >>= 1
    return drives

if __name__ == '__main__':
    synchronize()
