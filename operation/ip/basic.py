#!/usr/bin/python
# -*- encoding:utf8 -*-
__author__ = 'qianqinbo'

import IPy;
from IPy import IP;
#Ip版本
print(IP('10.0.0.0/8').version())
print(IP('::1').version())

ip = IP('192.168.0.0/16')
#这个网段的IP个数
print(ip.len())
#这个网段的所有IP清单
#for x in ip:
    #print(x)

#反向解析名称
ip = IP('120.26.112.178')
print(ip.reverseName())

print(IP('120.26.112.178').iptype())

print(IP('192.168.32.3').iptype())

print(IP('8.8.8.8').int())
print(IP('8.8.8.8').strHex())
print(IP('8.8.8.8').strBin())
print(IP(0x8080808))
#根据IP与掩码生成网段格式
print(IP('192.168.1.0').make_net('255.255.255.0'))
print(IP('192.168.1.0/255.255.255.0', make_net=True))
print(IP('192.168.1.0-192.168.1.255', make_net = True))
#定制不同输出类型的网段
print(IP('192.168.1.0/24').strNormal(0))
print(IP('192.168.1.0/24').strNormal(1))
print(IP('192.168.1.0/24').strNormal(2))
print(IP('192.168.1.0/24').strNormal(3))
