import pyautogui as gui
import time
import math

""" Main Functions """
# Move Mouse to safe area on the page
def safe_zone():
    gui.moveTo(150, 200, duration=1)
    gui.scroll(1000)
    time.sleep(1)
    gui.click()

# Pauses when scene freezes
def scene_frozen():
    not_responding = True
    while not_responding == True:
        frozen = gui.locateOnScreen('items/not-responding.PNG', confidence=0.9)
        if frozen == None:
            time.sleep(0.3)
            break