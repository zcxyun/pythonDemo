#!/usr/bin/env
# -*- coding: utf-8 -*-

import csv
# import codecs
# with codecs.open('resource/example.csv', 'r', 'utf-8') as originFile:
with open('origin.csv', encoding='utf-8') as originFile:
  originReader = csv.reader(originFile, delimiter=' ')
  originData = list(originReader)
  print(originData)

