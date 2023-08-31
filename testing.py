import pyautogui
import time


# Get mouse position
def get_mouse_position():
    mouse_pos = pyautogui.position()
    print(mouse_pos)


def test_code():
    # Return to main page
    back_btn = pyautogui.locateOnScreen('items/back.PNG')
    back_btn_ctr = pyautogui.center(back_btn)
    pyautogui.moveTo(back_btn_ctr, duration=0.5)
    pyautogui.click()


test_code()
