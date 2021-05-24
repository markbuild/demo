#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author Mark Li(https://github.com/markbuild)
# Function: Count doku pages

import os
import re
import colorprint

from ctypes import windll

dokupages = 0

def countdokupages():
    global dokupages
    dokupagedir= 'C:\\markli\\tool\\markbuild\\doku\\data\\pages'
    _countpages(dokupagedir)

    colorprint.color_print('Total:' + str(dokupages) + ' pages','pink')

#Synchronnize to backup
def _countpages(aim_dir):
    global dokupages
    os.chdir(aim_dir) # Changes the current working directory to orginal directory 
    listdir = os.listdir()
    for name in listdir: # Directory traversal
        if len(re.findall(r'\.txt$',name))>0 :
            dokupages=dokupages+1
            colorprint.color_print(str(dokupages) + '：' + aim_dir+'\\'+name,'skyblue')
            continue
        if os.path.isdir(aim_dir+'\\'+name):# If directory
            _countpages(aim_dir+'\\'+name) # Recursion/递归

if __name__ == '__main__':
    countdokupages()
