#!/usr/bin/python
# -*- encoding:utf8 -*-
__author__ = 'qianqinbo'

import psutil
mem = psutil.virtual_memory()
#获取内存完整信息
print(mem)
#内存总数
print(mem.total)
#获取空闲内存数
print(mem.free)
#获取SWAP分区信息
print(psutil.swap_memory())