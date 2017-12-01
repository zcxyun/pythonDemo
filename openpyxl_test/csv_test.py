#!/usr/bin/env
# -*- coding: utf-8 -*-

import csv
import openpyxl
import itertools
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

moneyIter = iter(money)
payeeIter = iter(payee)
payeeNumberIter = iter(payeeNumber)
firstPayDateIter = iter(firstPayDate)

wb = openpyxl.load_workbook('test.xlsx')
sheet = wb.get_sheet_by_name('sheet')
sheetTemplate = wb.get_sheet_by_name('sheetTemplate')
# 计数
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= len(money), natuals)
# csv 文件中的数据根据一定的规则复制到相应的 Excel 文件中
def copy(sheet):
  try:
    print(sheet.title)
    for rowOfCellObjects in sheet['B2':'H31']:
      for index, cell in enumerate(rowOfCellObjects):
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
            cell.value = rowOfCellObjects[0].value
          if index == 5:
            cell.value = rowOfCellObjects[2].value
    # if sheet['A31'].value:
    ws_next = wb.copy_worksheet(sheetTemplate)
    ws_next.title = sheetTemplate.title[:5] + str(next(ns))
    copy(ws_next)
  except StopIteration as e:
    return
copy(sheet)
# 根据前一个工作表的索引建立新工作表的索引
def makeIndex():

  sheet1 = wb.get_sheet_by_name('sheet1')
  sheet1['A2'] = sheet['A31'].value + 1
  print(sheet1['A2'].value)
  for i in range(len(sheet1['A2':'A31'])):
    if i >= 1:
      sheet1['A2':'A31'][i][0].value = sheet1['A2':'A31'][i-1][0].value + 1

makeIndex()
wb.save('test.xlsx')


