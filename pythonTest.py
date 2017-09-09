##import os
##L = [('Bob', 88), ('Adam', 88), ('Bart', 88), ('Lisa', 88),]
##filelist = [f for f in os.listdir('.')]
##print(filelist)
# from functools import reduce
# def add(x,y):
#     return x + y
# print(list(range(10))[::2])
# print(reduce(add, range(10)[::2]))

# 根据今天什么班计算未来某一天是什么班
import time
def workday(someworkOfToday, someday):
  workkind = 'sdfsdf'
  today = time.localtime()
  dt = time.strptime(someday, '%Y-%m-%d')
  # print(today.tm_yday)
  # print(dt.tm_yday)
  timeInterval = abs(today.tm_yday - dt.tm_yday)
  # print(timeInterval % 5)
  someworkList = ['xingZhengBan', 'zhuBan', 'yeBan', 'xiuXi_1', 'xiuXi_2']
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
  return workkind
todayWork = input('please input your workname of today:')
furDay = input('please input your someday like 2017-9-9:')
print('Your workkind of %s is %s' % (furDay, workday(todayWork, furDay)))


