#!/usr/bin/python
# -*- encoding:utf8 -*-
__author__ = 'qianqinbo'

import psutil
from subprocess import PIPE
#通过psutil的Popen方法启动的应用程序，可以跟踪该程序运行的所有相关信息
p = psutil.Popen(["/usr/bin/python","-c","print('hello')"])
print(p.name())

print(p.username())

print(p.cpu_times())