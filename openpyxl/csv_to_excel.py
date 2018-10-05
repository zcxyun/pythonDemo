#!/usr/bin/env
# -*- coding: utf-8 -*-

import csv
import re
import openpyxl
import itertools
from datetime import datetime
# from openpyxl.utils import get_column_letter, column_index_from_string

money = []
payee = []
payeeNumber = []
firstPayDate = []

#with open('resource/example.csv', encoding='utf-8') as originFile:
# 将csv文件的数据提取到相应的列表中
with open('E:/新农合银行转账统计表/新农合网银统计银行下载原件/12.1-12.4.csv', encoding='utf-16') as originFile:
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
        firstPayDate.append(fpd[index][:10])

# 将相应的列表转换为相应的迭代器
moneyIter = iter(money)
payeeIter = iter(payee)
payeeNumberIter = iter(payeeNumber)
firstPayDateIter = iter(firstPayDate)

# 加载 excel 文件
wb = openpyxl.load_workbook('E:/新农合银行转账统计表/2017-12-01至2017-12-31.xlsx')
# 获取工作表
sheet0 = wb.get_sheet_by_name('sheet0')
# 获取工作表模板
sheetTemplate = wb.get_sheet_by_name('sheetTemplate')
# 计数器
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= len(money), natuals)
# csv 文件中的数据根据一定的规则复制到相应的 Excel 文件中
def copy(sheet):
  try:
    # print(sheet.title)
    for rowOfCellObjects in sheet['B5':'H34']:
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
          # if index == 6:
          #   cell.value = datetime.now().date()
    ws_next = wb.copy_worksheet(sheetTemplate)
    ws_next.title = sheetTemplate.title[:5] + str(next(ns))
    copy(ws_next)
  except StopIteration as e:
    return

copy(sheet0)
# 根据前一个工作表的索引建立新工作表的索引
def makeIndex(sheet):
  title = re.match(r'^([a-zA-Z]+)(\d+)$', sheet.title)
  titleStr = title.group(1)
  titleExt = title.group(2)
  titleExtToInt = int(titleExt)
  # print(str(titleExtToInt+1))
  sheetPrev = wb.get_sheet_by_name(titleStr + str(titleExtToInt-1))
  # print(sheetPrev)
  sheet['A5'] = sheetPrev['A34'].value + 1
  # print(sheet['A2'].value)
  for i in range(len(sheet['A5':'A34'])):
    if i >= 1:
      sheet['A5':'A34'][i][0].value = sheet['A5':'A34'][i-1][0].value + 1

# 合计支付金额
def moneySum(sheet):
  sheet['D35'] = "=SUM(D5:D34)"
  sheet['G35'] = "=SUM(G5:G34)"

for sh in wb:
  moneySum(sh)
  if sh.title != 'sheetTemplate' and sh.title != 'sheet0' :
    makeIndex(sh)

wb.save('E:/新农合银行转账统计表/2017-12-01至2017-12-31.xlsx')
