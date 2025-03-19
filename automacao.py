import pyautogui
import time

pyautogui.press("winleft")
time.sleep(1)
pyautogui.write("word")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.typewrite("Parabens Manu!", interval=0.1)
time.sleep(1)
pyautogui.press("left", presses=7)
time.sleep(1)
pyautogui.hotkey("shift", "F10")
time.sleep(1)
pyautogui.press("enter")