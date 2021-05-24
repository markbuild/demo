#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author Mark Li(https://github.com/markbuild)
# Function:校验软件哈希值
import os
import xml.sax.saxutils
import hashlib
import colorprint

def md5sha():
    colorprint.color_print("Input file path eg:C:\\Users\\Mark\\OneDrive\\pirate\\taotie\\Shadowsocks.exe",'yellow')
    exefile = input(">>")
    md5res = hashlib.md5(open(exefile,'rb').read()).hexdigest()
    colorprint.color_print("\nMD5: %s" % md5res, 'pink')
    sha1res = hashlib.sha1(open(exefile,'rb').read()).hexdigest()
    colorprint.color_print("\nSHA-1: %s" % sha1res, 'pink')
    sha256res = hashlib.sha256(open(exefile,'rb').read()).hexdigest()
    colorprint.color_print("\nSHA-256: %s" % sha256res, 'pink')
    sha512res = hashlib.sha512(open(exefile,'rb').read()).hexdigest()
    colorprint.color_print("\nSHA-512: %s" % sha512res, 'pink')
            
if __name__ == '__main__':
    md5sha()
