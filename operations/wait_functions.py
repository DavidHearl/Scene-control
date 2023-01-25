import pyautogui, time, math

""" Main Functions """
# Move Mouse to safe area on the page
def safe_zone():
    pyautogui.moveTo(150, 200, duration=1)
    pyautogui.scroll(1000)
    time.sleep(1)
    pyautogui.click()

# Wait for Project to close
def wait_close():
    project_closed = False
    not_responding = True
    while project_closed == False or not_responding == True:
        closing_project = pyautogui.locateOnScreen('items/closing-project.PNG', confidence=0.9)
        frozen = pyautogui.locateOnScreen('items/not-responding.PNG', confidence=0.9)
        if closing_project == None and frozen == None:
            project_closed = True
            not_responding = False
            time.sleep(1)
            break

# Wait for project to open
def wait_open():
    project_opened = False
    not_responding = True
    while project_opened == False or not_responding == True:
        opening_project = pyautogui.locateOnScreen('items/opening-project.PNG', confidence=0.9)
        frozen = pyautogui.locateOnScreen('items/not-responding.PNG', confidence=0.9)
        if opening_project == None and frozen == None:
            project_closed = True
            not_responding = False
            time.sleep(1)
            break

# Pauses when scene freezes
# def scene_frozen():
#     not_responding = True
#     while not_responding == True:
#         frozen = gui.locateOnScreen('items/not-responding.PNG', confidence=0.9)
#         if frozen == None:
#             time.sleep(0.3)
#             break      
