import pyautogui
import time


# Get mouse position
def get_mouse_position():
    mouse_pos = pyautogui.position()
    print(mouse_pos)


def code():
    processed_folder_path = "E:\XXX - Test - Processed"

    # Click to the left of the drop down arrow
    drop_down_btn = pyautogui.locateOnScreen('items/previous-location.png')
    drop_down_btn_pos = pyautogui.center(drop_down_btn)
    drop_down_btn_pos = (drop_down_btn.left - 20, drop_down_btn_pos[1])

    pyautogui.moveTo(drop_down_btn_pos, duration=0.5)
    pyautogui.click()
    time.sleep(0.5)

    # Paste the link
    pyautogui.typewrite(processed_folder_path)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)

    # Click select folder
    select_folder_btn = pyautogui.locateOnScreen('items/select-folder.png')
    select_folder_btn_ctr = pyautogui.center(select_folder_btn)
    pyautogui.moveTo(select_folder_btn_ctr, duration=0.5)
    pyautogui.click()

    # Return to main page
    back_btn = pyautogui.locateOnScreen('items/back.PNG')
    back_btn_ctr = pyautogui.center(back_btn)
    pyautogui.moveTo(back_btn_ctr, duration=0.5)
    pyautogui.click()

    # Click project transfer button
    project_transfer_btn = pyautogui.locateOnScreen('items/project-transfer.PNG')
    project_transfer_btn_ctr = pyautogui.center(project_transfer_btn)
    pyautogui.moveTo(project_transfer_btn_ctr, duration=0.5)
    pyautogui.click()


code()
