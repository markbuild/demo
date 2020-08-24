#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author Mark Li(https://github.com/markbuild)
# Function:Scan some important port

import socket
import os
import colorprint

def tcpscan(ports,address):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #Create a socket, AF_INET for IPv4，AF_INET6 for IPv6
        for port in ports:
            try:
                s.connect((address,port))
                colorprint.color_print('{} Open - {}'.format(port,ports[port]),'red')
            except:
                colorprint.color_print('{} Close - {}'.format(port,ports[port]),'green')
        s.close() #Close network connect
def udpscan(ports,address):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        for port in ports:
            try:
                s.sendto(b'Hello',('127.0.0.1', port))
                data = s.recv(1024)
                colorprint.color_print('{} Open - {}'.format(port,ports[port]),'red')
            except:
                colorprint.color_print('{} Close - {}'.format(port,ports[port]),'green')
        s.close()

def scanmyport():
    address = '127.0.0.1'
    tcpports = {80:'HTTP',135:'RPC(远程过程调用)服务',139:'获得NetBIOS/SMB服务-文件和打印机共享',445:'在局域网中访问共享文件夹或共享打印机',593:'#',2745:'#',3127:'#',6129:'远程控制软件(dameware nt utilities)服务端监听端口',3389:'远程桌面'}
    udpports = {135:'RPC(远程过程调用)服务',137:'在局域网中提供计算机的名字或IP地址查询服务，一般安装了NetBIOS协议后，该端口会自动处于开放状态',138:'端口的主要作用就是提供NetBIOS环境下的计算机名浏览功能',139:'获得NetBIOS/SMB服务-文件和打印机共享',
                445:'在局域网中访问共享文件夹或共享打印机'}
    colorprint.color_print('-'*50,'yellow')
    colorprint.color_print('TCP：','yellow')
    tcpscan(tcpports,address)
    colorprint.color_print('UDP：','yellow')
    udpscan(udpports,address)
    colorprint.color_print('-'*50,'yellow')
    
if __name__ == '__main__':
    scanmyport()
