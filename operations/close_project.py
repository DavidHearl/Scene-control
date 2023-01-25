import pyautogui, time

def close_project():
    """ Check if a project is currently open """
    close_project = pyautogui.locateCenterOnScreen('./items/close-project.PNG', confidence=0.9)
    if close_project != None:
        pyautogui.moveTo(close_project, duration=1)
        pyautogui.click()
        time.sleep(2)
    else:
        print("        There are no projects currently open")
        print("")
