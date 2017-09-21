#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

import os

def listFilesAtPath(path, some_str='.py'):
    return [x for x in os.listdir(path) if os.path.isfile('%s/%s' % (path, x)) and some_str in x]
def listAllFilesAtPath(path, some_str='.py'):
    file_list = []
    for i in os.listdir(path):
        if os.path.isdir('%s/%s' % (path, i)):
            listAllFilesAtPath('%s/%s' % (path, i), some_str)
    file_list = listFilesAtPath(path, some_str)
    if file_list != []:
        print(path)
        print(file_list)

listAllFilesAtPath('D:/developer/pythonDemo','str')
