#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

import os

def listFilesAtPath(path):
    return [x for x in os.listdir(path) if os.path.isfile('%s/%s' % (path, x)) and '.py' in x]
def listAllFilesAtPath(path):
    for i in os.listdir(path):
        if os.path.isdir('%s/%s' % (path, i)):
            listAllFilesAtPath('%s/%s' % (path, i))
    print(path)
    print(listFilesAtPath(path))

listAllFilesAtPath('E:/developer/pythonDemo')
