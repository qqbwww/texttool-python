#!/usr/bin/python
# -*- encoding:utf8 -*-
__author__ = 'qianqinbo'

import  psutil
print(psutil.disk_partitions())
#获取分区的的使用情况
print(psutil.disk_usage("c:\\"))
#硬盘总IO次数
print(psutil.disk_io_counters())
#获取单个分区IO个数，读写信息
print(psutil.disk_io_counters(perdisk=True))