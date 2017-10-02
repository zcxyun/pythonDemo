#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import openpyxl

wb = openpyxl.load_workbook('test.xlsx')
# print(type(wb))
# print(wb.get_sheet_names())
sheet = wb.get_sheet_by_name('Sheet1')
# print(sheet)
# print(type(sheet))
# print(sheet.title)
# anotherSheet = wb.get_active_sheet()
# print(anotherSheet)

# print(sheet['A1'])
# print(sheet['A1'].value)
# print(type(sheet['A1'].value))

# c = sheet['B1']
# print('Row: ' + str(c.row) + ', Column: ' + c.column + ' is: ' + c.value)
# print('Cell ' + c.coordinate + ' is ' + c.value)

# for i in range(1,8,2):
#   print(i, sheet.cell(row=i, column=2).value)

# print(sheet.get_highest_row())
# print(sheet.get_highest_column())

