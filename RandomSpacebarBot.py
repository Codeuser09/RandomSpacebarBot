from pyautogui import *
import pyautogui
import time
import keyboard
import random

time.sleep(5)

while not keyboard.is_pressed('k'):
    time.sleep(0.5)

    action = random.randint(0, 1)

    if action == 1:
        keyboard.press('space')

    if action == 0:
        keyboard.release('space')
