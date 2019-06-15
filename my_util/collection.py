 from itertools import chain
from collections import Iterable

# b = [[1,2, {'a': 1}, [3, {2,3, 'abc'}]], [3,4, (11, 22, '33')],[5,6, [7,8]], 'sdfsdf']

# # 展开一级可迭代对象
# print(list(chain.from_iterable(b)))

# # 逐级展开所有可迭代对象
# def flatlist(inlist, outlist):
#     for i in inlist:
#         # 判断 i 是不是字符串类型， 并且长度要 大于 1, 单一字符串会导致无限递归
#         if isinstance(i, str) and len(i) > 1:
#             flatlist(i, outlist)
#         # 判断 i 是不是可迭代类型，并且去除掉单一字符串这一可迭代类型，单一字符串会导致无限递归
#         elif isinstance(i, Iterable) and not isinstance(i, str):
#             flatlist(i, outlist)
#         else:
#             outlist.append(i)
#     return outlist

# # 测试
# print(flatlist(b, []))


# counter groupby可以实现不同元素的分组  ===================================
from collections import Counter
from itertools import groupby

c2 = Counter('zcxzcxzcxlskdjjfkdjyiiuiuiuiuiusdyfekljreysdfkshdjkfhs')
order_c2 = ''.join(list(c2.elements()))
group_c2 = groupby(order_c2)
print('c2 = ', c2)
print('order_c2 = ', order_c2)
print('c2.most_common() = ', c2.most_common())
print('dict(c2) = ', dict(c2))
print('group_c2 = ', group_c2)
for i, group in group_c2:
    print(i, list(group))
