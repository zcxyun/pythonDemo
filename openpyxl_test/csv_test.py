#!/usr/bin/env
# -*- coding: utf-8 -*-

import csv
# import codecs
# with open('resource/example.csv') as originFile:
with open('origin.csv', encoding='utf-8') as originFile:
  exampleReader = csv.reader(originFile)
  exampleData = list(exampleReader)
  print(exampleData)
