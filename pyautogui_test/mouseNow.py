#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# mouseNow.py - Display the mouse cursor's current position

import pyautogui
print('Press Ctrl-C to quit.')
try:
  while True:
    # TODO: Get and print the mouse coordinates.
    x, y = pyautogui.position()
    pixelColor = pyautogui.screenshot().getpixel((x,y))
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
    positionStr += ', ' + str(pixelColor[1]).rjust(3)
    positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
    print(positionStr, end='')
    print('\b' * len(positionStr), end='', flush=True)

except KeyboardInterrupt:
  print('\nDone.')
