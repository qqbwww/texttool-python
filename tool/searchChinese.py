#!usr/bin/python
# -*- encoding: utf8 -*-

import os
import sys
import re

def wc(file_name):
    chinese = re.compile(ur'[\u4e00-\u9fa5]+')
    fo = open(file_name);
    count = 0
    lineNo = 0
    for line in fo:
            lineNo += 1
            linec = line.decode("UTF-8")
            for n in chinese.findall(linec):
                print ((n +" at:" + unicode(lineNo)).encode("utf-8"))
    fo.close()

def listyourdir(level,path,reg):
    for i in os.listdir(path):
        m = re.search(reg,i)
        if( m != None):
            print ('  '*(level+1) + i)
            wc(path + '\\' + i)
        if os.path.isdir(path + '\\' + i):
            listyourdir(level+1,path+ '\\' + i,reg)




rootpath = 'D:/'
f = open('d:/filedir.txt','w+')
sys.stdout = f
listyourdir(0,rootpath,'[.](vm|js|java)$')
f.close()
