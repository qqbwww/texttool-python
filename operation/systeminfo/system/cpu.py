#!/usr/bin/python
# -*- encoding:utf8 -*-
import psutil
print(psutil.cpu_times())
#获取CPU完整信息
print(psutil.cpu_times(True))
#获取单项数据
print(psutil.cpu_times().user)
#获取CPU逻辑个数
print(psutil.cpu_count())
#获取CPU物理个数
print(psutil.cpu_count(logical=False))