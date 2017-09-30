#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pyautogui, time

time.sleep(5)
pyautogui.click() # click to put drawing program in focus
distance = 200
while distance > 0:
  pyautogui.dragRel(distance, 0, duration=0.1) # move right
  distance -= 5
  pyautogui.dragRel(0, distance, duration=0.1) # move down
  pyautogui.dragRel(-distance, 0, duration=0.1) # move left
  distance -= 5
  pyautogui.dragRel(0, -distance, duration=0.1) # move up

