#!/usr/bin/env
# -*- coding:utf-8 -*-

# weird_board = [['_'] * 3 for i in range(3)]
# print(weird_board)
# weird_board[1][2] = 'X'
# print(weird_board)

# weird_board_2 = [['_'] * 3] * 3
# print(weird_board_2)
# weird_board_2[1][2] = 'X'
# print(weird_board_2)

l = [1,2,3]
print(id(l))
l *= 3
print(id(l))
t = (1,3,4)
print(id(t))
t *= 3
print(id(t))
