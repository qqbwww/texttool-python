#!/usr/bin/python
# -*- encoding:utf8 -*-

import re
import glob

def wc(file_name):
    chinese = re.compile(ur'[\u4e00-\u9fa5]+')
    fo = open(file_name);
    count = 0
    lineNo = 0
    for line in fo:
        lineNo += 1
        linec = line.decode("UTF-8")
        for n in chinese.findall(linec):
            print (n +" at:" + str(lineNo))
    fo.close()
    return count


def wcu(file_name):
    sets = set()
    chinese = re.compile('=([\u4e00-\u9fa5]+)')
    fo = open(file_name);
    count = 0
    lineNo = 0
    for line in fo:
        lineNo += 1
        for n in chinese.findall(line):
            #print (n +" at:" + str(lineNo))
            sets.add(n.decode("unicode_escape"))
    fo.close()
    return sets


def getChinese(chineseset):
    totalsets = set()
    fileList=glob.glob("D:/work/*.properties")
    for filename in fileList:
        sets = wcu(filename)
        #print sets
        totalsets = totalsets.union(wcu(filename))
    return totalsets


sets = getChinese(chineseset)
for n in sets:
    print n

