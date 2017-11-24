# 根据今天什么班计算未来某一天是什么班
import time
def workday(someworkOfToday, someday):
  workkind = ''
  today = time.localtime()
  dt = time.strptime(someday, '%Y-%m-%d')
  # print(today.tm_yday)
  # print(dt.tm_yday)
  timeInterval = dt.tm_yday - today.tm_yday
  # someworkList = ['行政班', '主班', '夜班', '第一天休息', '第二天休息']
  someworkList = ['xz', 'zb', 'yb', 'xx1', 'xx2']
  for x in range(5):
    if someworkList[x] == someworkOfToday:
      if (timeInterval % 5) == 0:
        workkind = someworkList[x]
      elif (timeInterval % 5) == 1:
        workkind = someworkList[x+1 if x+1<=4 else x+1-5]
      elif (timeInterval % 5) == 2:
        workkind = someworkList[x+2 if x+2<=4 else x+2-5]
      elif (timeInterval % 5) == 3:
        workkind = someworkList[x+3 if x+3<=4 else x+3-5]
      elif (timeInterval % 5) == 4:
        workkind = someworkList[x+4 if x+4<=4 else x+4-5]
      elif (timeInterval % 5) == -1:
        workkind = someworkList[x-1 if x-1>=0 else x-1+5]
      elif (timeInterval % 5) == -2:
        workkind = someworkList[x-2 if x-2>=0 else x-2+5]
      elif (timeInterval % 5) == -3:
        workkind = someworkList[x-3 if x-3>=0 else x-3+5]
      elif (timeInterval % 5) == -4:
        workkind = someworkList[x-4 if x-4>=0 else x-4+5]
  return workkind
##todayWork = input('please input your workname of today:')

todayWork = input('请输入当前工作日名称(拼音首字母，例如行政班:xz, 主班: zb, 夜班: yb, 休息1: xx1, 休息2: xx2) 回车键确认:')
##furDay = input('please input your someday like 2017-9-9:')

furDay = input('请输入日期像这样 2017-9-9 回车键确认:')
##print('Your workkind of %s is %s' % (furDay, workday(todayWork, furDay)))

print('你 %s 的工作日是 %s' % (furDay, workday(todayWork, furDay)))


