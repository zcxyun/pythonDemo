# # 枚举 ===============================================================
from enum import Enum
from enum import IntEnum,unique
# @unique
# class Vip(IntEnum):
#   RED = 1
#   YELLOW = 1
#   BLUE = 3
# print(Vip.YELLOW)

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name, member in Month.__members__.items():
    # print(name, '=>', member, ',', member.value)
for item in Month:
  print(item)

@unique
class Weekday(Enum):
  Sun = 0
  Mon = 1
  Tue = 2
  Wed = 3
  Thu = 4
  Fri = 5
  Sat = 6
# for name, member in Weekday.__members__.items():
  # print(name, '=>', member, ',', member.value)

# print(type(Weekday.Sun) == Weekday)

# try:
# print(Weekday(9))
# except Exception as e:
  # print(str(e))
