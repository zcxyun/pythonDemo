import pandas as pd
import os
class Sift:
  ''' 把工作薄第一个工作表根据列名筛选到以列名命名的文件夹中，
      文件夹中的所有文件名是以某列数据去重后命名的，
      数据也是筛选后的数据。
  '''
  def __init__(self, workbook_path):
    self.workbook = pd.read_excel(workbook_path)
    self.col_names = list(self.workbook.keys())

  def makedir(self, key):
    '''根据列名创建文件夹'''
    if key:
      sift_dir = '筛选_{}'.format(key)
      print(sift_dir)
      os.makedirs(sift_dir, exist_ok=True)
      return sift_dir
    return False
  def get_col_to_uni(self, col_name):
    '''获取工作表某一列的去重数据'''
    if col_name in self.col_names:
      return self.workbook.drop_duplicates(col_name)[col_name]
    return False
  def sift(self, *keys):
    '''根据传入的列名开始筛选到不同文件夹'''
    for key in keys:
      col_data = self.get_col_to_uni(key)
      print(list(col_data))
      if not list(col_data):
        print('没有 {} 列数据'.format(key))
        continue
      sift_dir = self.makedir(key)
      if sift_dir:
        for sift_name in col_data:
          res = self.workbook[self.workbook[key] == sift_name]
          sift_name = '{}.xlsx'.format(sift_name)
          path = os.path.join(sift_dir, sift_name)
          res.to_excel(path)

# 在下面输入要筛选的工作薄名称
workbook_path = 'zcx.xlsx'
sift = Sift(workbook_path)
# 在下面输入列名
sift.sift('涉案银行','录入单位')
