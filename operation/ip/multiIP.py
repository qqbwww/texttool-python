#!/usr/bin/python
# -*- encoding:utf8 -*-
__author__ = 'qianqinbo'

import IPy;
from IPy import IP

print (IP('10.0.0.0/24') < IP('12.0.0.0/24'))

# 判断IP地址和网段是否包含于另一个网段中

print('192.168.1.100')