#! /usr/bin/env python3
# -*- coding: utf-8 -*-

my_list = [12, 5, 13, 8, 9, 65, 1, 2,6]

# def bubble(bad_list):
#     length = len(bad_list) - 1
#     sorted = False

#     while not sorted:
#         sorted = True
#         for i in range(length):
#             if bad_list[i] > bad_list[i+1]:
#                 sorted = False
#                 bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]
# my_list = [12, 5, 13, 8, 9, 65,1]

def bubble(bad_list):
  length = len(bad_list) - 1
  for j in range(length):
    for i in range(length):
      if bad_list[i] > bad_list[i+1]:
        bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]

bubble(my_list)
print (my_list)
