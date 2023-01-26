import pyautogui, time

def load_projects():
    # Check to see if the project is empty
    no_projects = pyautogui.locateOnScreen('items/no-projects.PNG')
    if no_projects == None:
        settings = pyautogui.locateCenterOnScreen('./items/settings-wheel.PNG', confidence=0.9)
        print("Moving to settings...")
        print("")
        pyautogui.moveTo(settings, duration=1)
        time.sleep(1)
        pyautogui.click()
    else:
        print("No folders present...")
        print("")

def close_project():
    close_project = pyautogui.locateCenterOnScreen('./items/close-project.PNG', confidence=0.9)
    if close_project != None:
        pyautogui.moveTo(close_project, duration=1)
        pyautogui.click()
        print("Waiting 2 seconds...")
        print("")
        time.sleep(2)
    else:
        print("There are no projects currently open...")
        print("")

def save_changes():
    save_changes = pyautogui.locateOnScreen('items/save-changes.PNG')
    if save_changes != None:
        pyautogui.locateCenterOnScreen('items/yes.PNG')
        pyautogui.click()
        print("Waiting 1 second...")
        time.sleep(1)
        pyautogui.locateCenterOnScreen('items/ok-button.PNG')
        pyautogui.click()
        pyautogui.locateCenterOnScreen('items/ok-button.PNG')
        pyautogui.click()
