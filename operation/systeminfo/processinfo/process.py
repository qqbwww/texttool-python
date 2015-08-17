#!/usr/bin/python
# -*- encoding:utf8 -*-

import psutil
#列出所有的进程PID
print(psutil.pids())
#实例化一个Process对象，参数为一进程PID
p = psutil.Process(5812)
#进程名称
print(p.name())
#进程的执行路径
print(p.exe())
#进程工作目录绝对路径
print(p.cwd())
#进程状态
print(p.status())
#进程创建时间
print(p.create_time())
#进程uid(Window好像有问题)
#print(p.uids())
#进程gid
#print(p.gids())
#进程cpu时间
print(p.cpu_times())
#进程cpu亲和度
print(p.cpu_affinity())
#进程内存利用率
print(p.memory_percent())
#进程内存rss、vms信息
print(p.memory_info())
#进程io信息
print(p.io_counters())
print(p.connections())
print(p.threads())