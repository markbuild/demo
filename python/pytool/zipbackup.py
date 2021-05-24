#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author Mark Li(https://github.com/markbuild)
# Function: zip backup

import os, zipfile, re, time
import colorprint
from ctypes import windll
import string

def zipbackup():
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

    zipfilename = removable_disk_volume+":\\zipbackup\\"+time.strftime('%Y-%m-%d')+".zip"
    folders_to_zip = ["C:\\Users\\Mark\\OneDrive\\design",
                      "C:\\markli\\github",
                      "C:\\Users\\Mark\\OneDrive\\time"]

    f = zipfile.ZipFile(zipfilename, 'w', zipfile.ZIP_DEFLATED)

    for folder in folders_to_zip:
        colorprint.color_print("processing: " + folder,'yellow')
        for dirpath, dirnames, filenames in os.walk(folder):
            if re.search(r'\\\.git',dirpath): #fitler .git folder
                continue
            for filename in filenames:
                f.write(os.path.join(dirpath,filename)) 
    f.close()

    colorprint.color_print('Zip completed','pink')

def _getDrives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_lowercase:
        if bitmask & 1 and letter !='c':
            drives.append(letter)
        bitmask >>= 1
    return drives

if __name__ == '__main__':
    zipbackup()
