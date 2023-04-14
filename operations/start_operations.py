import pyautogui, time
import tkinter
import os
import json

def startup():
    # Introduction
    print("")
    print("----------------------------------------------------------")
    print("-----------Welcome to Automatic Scan Processing-----------")
    print("----------------------------------------------------------")
    print("")

    # # Get screen size
    # print(pyautogui.size())
    # print("")

    # # Calculate position for mouse test
    # screen_width, screen_height = pyautogui.size()
    # positionX0, positionY0 = (screen_width - screen_width + 100), (screen_height - screen_height + 100)
    # positionX1, positionY1 = (screen_width - 100), (screen_height - screen_height + 100)
    # positionX2, positionY2 = (screen_width - 100), (screen_height - 100)
    # positionX3, positionY3 = (screen_width - screen_width + 100), (screen_height - 100)

    # # Loop though positions
    # print("Moving Mouse to", positionX0,",", positionY0, "...")
    # pyautogui.moveTo(positionX0, positionY0, duration=0.5)

    # print("Moving Mouse to", positionX1,",", positionY1, "...")
    # pyautogui.moveTo(positionX1, positionY1, duration=0.5)

    # print("Moving Mouse to", positionX2,",", positionY2, "...")
    # pyautogui.moveTo(positionX2, positionY2, duration=0.5)

    # print("Moving Mouse to", positionX3,",", positionY3, "...")
    # pyautogui.moveTo(positionX3, positionY3, duration=0.5)

    # print("")
    # print("Did the mouse move on the correct screen ? (Y/N)")

    # print("")
    # main_screen = input()


def folder_setup():
    print("Please Choose the directory that contains the scans")
    time.sleep(0.2)
    print("")

    # Ask user to Select Directory
    directory = tkinter.filedialog.askdirectory()
    print("Selected Directory:", directory)
    time.sleep(1)
    print("")

    # Create an array
    outer_keys = []
    inner_keys = [
        'processed',
        'registered',
        'aligned',
        'point_cloud',
        'clean_up',
        'rcp_export',
        'rcs_export',
        'uploaded'
    ]
    inner_value = False

    # List all files in the directory
    directory_content = os.listdir(directory)
    print("Number of items : ", len(directory_content))
    print("")
    for x in directory_content:
        outer_keys.append(x)

    # Create a nested dictionary
    nested_dict = {
        outer_key: {
            inner_key: inner_value
            for inner_key in inner_keys
        }
        for outer_key in outer_keys
    }
    
    # nested_dict["adagio"]["processed"] = True

    # Print it to console in a readable format
    print(json.dumps(nested_dict, indent=4))

def check_scene_open():
    print("Checking if SCENE is open...")
    print("")

    time.sleep(0.5)

    scene_open = pyautogui.locateCenterOnScreen("./items/scene-icon.PNG", confidence=0.9)
    if scene_open == None:
        print("Scene is NOT open, opening now...")
        print("")
        windows_search = pyautogui.locateCenterOnScreen("items/windows-search.PNG")
        pyautogui.moveTo(windows_search, duration=0.5)
        pyautogui.click()
        pyautogui.write('scene', interval=0.1)
        pyautogui.hotkey('enter')
        close_button = None
        while close_button == None:
            print("Waiting for Scene to load...")
            print("")
            time.sleep(3)
            close_button = pyautogui.locateCenterOnScreen("items/close.PNG")
            if close_button != None:
                break

        close = pyautogui.locateCenterOnScreen("items/close.PNG", confidence=0.9)
        pyautogui.moveTo(close, duration=1)
        pyautogui.click()
    else:
        print("Scene is already open...")
        print("")
