#!/usr/bin/python
# -*- encoding:utf8 -*-
__author__ = 'qianqinbo'

import psutil,datetime
#当前登录系统的用户信息
print(psutil.users())
#获取开机时间
print(psutil.boot_time())
#格式化时间
print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))