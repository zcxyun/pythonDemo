#!/usr/bin/env
# -*- coding: utf-8 -*-

import csv
import openpyxl
# from openpyxl.utils import get_column_letter, column_index_from_string

money = []
payee = []
payeeNumber = []
firstPayDate = []

##with open('resource/example.csv', encoding='utf-8') as originFile:
with open('origin.csv', encoding='utf-16') as originFile:
  originReader = csv.reader(originFile, delimiter='\t')
  originData = list(originReader)

  for index, title in enumerate(originData[0]):
    if title == '金额':
      for m in originData[1: len(originData)+1]:
        money.append(float(''.join(m[index].split(','))))
    if title == '收款人名称':
      for p in originData[1: len(originData)+1]:
        payee.append(p[index])
    if title == '收款人账号':
      for pn in originData[1: len(originData)+1]:
        payeeNumber.append(pn[index])
    if title == '初次委托日期':
      for fpd in originData[1: len(originData)+1]:
        firstPayDate.append(fpd[index])
# print(money)
# print(payee)
# print(payeeNumber)
# print(firstPayDate)

##  print(originData)
  # for row in originReader:
    # print("Row #" + str(originReader.line_num) + " " + str(row))
moneyIter = iter(money)
payeeIter = iter(payee)
payeeNumberIter = iter(payeeNumber)
firstPayDateIter = iter(firstPayDate)

wb = openpyxl.load_workbook('test.xlsx')
ws = wb.get_sheet_by_name('Sheet1')
i = 0
for rowOfCellObjects in ws['B2':'H31']:
  for index, cell in enumerate(rowOfCellObjects):
# for col in ws.iter.cols(min_row=1, max_col=9, max_row=31):
#   for cell in col:
    if cell.value == None:
      if index == 0:
        cell.value = next(payeeIter)
      if index == 1:
        cell.value = next(firstPayDateIter)
      if index == 2:
        cell.value = next(moneyIter)
      if index == 3:
        cell.value = next(payeeNumberIter)
      if index == 4:
        cell.value = next(payeeIter)
      if index == 5:
        cell.value = next(moneyIter)


    # for cellObjIndex in len(rowOfCellObjects):
    # if cellObjIndex == 1:
    # ws[cellObjIndex] = money[]
# ws['B23'].value = originData[1][1]
# ws['C23'].value = originData[1][4]
# ws['D23'].value = originData[1][0]
# ws['E23'].value = originData[1][2]
# ws['F23'].value = ws['B23'].value
# ws['G23'].value = ws['D23'].value

wb.save('test.xlsx')

