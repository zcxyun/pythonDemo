#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pyautogui, time

# 获取焦点
pyautogui.click(200,200)
pyautogui.typewrite('hello world!', 0.1)
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], 0.1)

pyautogui.keyDown('shift')
pyautogui.press('4')
pyautogui.keyUp('shift')

def commentAfterDelay():
  # pyautogui.click(200,200)
  # pyautogui.typewrite('\n')
  pyautogui.press('enter')
  pyautogui.typewrite('In IDLE, alt-3 comments out a line', 0.1)
  time.sleep(1)
  pyautogui.hotkey('ctrl', 'a')

commentAfterDelay()
