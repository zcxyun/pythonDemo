#!/usr/bin/env
# -*- coding: utf-8 -*-

import csv
import openpyxl
# from openpyxl.utils import get_column_letter, column_index_from_string

##with open('resource/example.csv', encoding='utf-8') as originFile:
with open('origin.csv', encoding='utf-16') as originFile:
  originReader = csv.reader(originFile, delimiter='\t')
  originData = list(originReader)
##  print(originData)
  # for row in originReader:
    # print("Row #" + str(originReader.line_num) + " " + str(row))

wb = openpyxl.load_workbook('test.xlsx')
ws = wb.get_sheet_by_name('Sheet1')
##for rowOfCellObjects in ws['B2':'H21']:
##  for cellObj in rowOfCellObjects:
##    print(cellObj.coordinate, cellObj.value)
##  print('--- END OF ROW ---')

ws['B23'].value = originData[1][1]
ws['C23'].value = originData[1][4]
ws['D23'].value = originData[1][0]
ws['E23'].value = originData[1][2]
ws['F23'].value = ws['B23'].value
ws['G23'].value = ws['D23'].value

wb.save('test3.xlsx')

