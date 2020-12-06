import pyautogui
import keyboard
import win32api, win32con
import time

"""
X:  553 Y:  539 RGB: ( 17,  17,  17)
X:  635 Y:  539 RGB: (255, 255, 255)
X:  713 Y:  533 RGB: (255, 255, 255)
X:  783 Y:  526 RGB: (255, 255, 255)
"""

X = 545 #rounded val
Y = (537, 613, 728, 820) #x and y mixed up
time.sleep(1)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while not keyboard.is_pressed('q'):
    if pyautogui.pixel(Y[0], X)[1] == 0:
        click(Y[0], X)
    if pyautogui.pixel(Y[1], X)[0] == 0:
        click(Y[1], X)
    if pyautogui.pixel(Y[2], X)[0] == 0:
        click(Y[2], X)
    if pyautogui.pixel(Y[3], X)[0] == 0:
        click(Y[3], X)



