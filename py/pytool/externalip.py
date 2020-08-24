#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author Mark Li(https://github.com/markbuild)
# Function: Get external IP
import urllib.request
import re
import colorprint

def externalip():
    url = 'http://www.ip138.com/ips1388.asp'
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    the_page = response.read().decode('gbk', 'ignore')
    result = re.findall(r'<td align="center">您的IP地址是：(.*)<br/><br/></td>',the_page)
    colorprint.color_print('-'*50,'yellow')
    colorprint.color_print('Your external IP:'+result[0],'yellow')
    colorprint.color_print('-'*50,'yellow')

if __name__ == '__main__':
    externalip()



