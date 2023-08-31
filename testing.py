import pyautogui
import time


# Get mouse position
def get_mouse_position():
    mouse_pos = pyautogui.position()
    print(mouse_pos)


def test_code():
    # Click select folder
    try:
        select_folder_btn = pyautogui.locateOnScreen('items/select-folder.png')
        if select_folder_btn:
            select_folder_btn_ctr = pyautogui.center(select_folder_btn)
            pyautogui.moveTo(select_folder_btn_ctr, duration=0.5)
            # pyautogui.click()
        else:
            print("Select folder button not found.")
    except pyautogui.ImageNotFoundException:
        print("Image 'select-folder.png' not found on the screen.")


# test_code()
get_mouse_position()
