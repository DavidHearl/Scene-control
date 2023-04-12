import pyautogui
import time

go = 1

while go == 1:
    pyautogui.moveTo(182,466, duration=2)
    time.sleep(60)
    pyautogui.click()
    time.sleep(60)
    pyautogui.moveTo(528, 340, duration=2)
    time.sleep(60)
    pyautogui.click()
