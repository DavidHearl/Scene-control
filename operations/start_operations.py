import pyautogui, time
import tkinter
import os
import json

def startup():
    print("")
    print("-------------------------------------------------------")
    print("-------------- Welcome to Scene Control ---------------")
    print("-------------------------------------------------------")
    print("")
    

def folder_setup():
    print("Please Choose the directory that contains the scans")
    print("")

    # Ask user to Select Directory
    directory = tkinter.filedialog.askdirectory()
    print(directory)
    print("")

    # Create an array
    outer_keys = []
    inner_keys = [
        'imported',
        'processed',
        'registered',
        'aligned',
        'point_cloud',
        'clean_up',
        'exported',
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
    
    # Print it to console in a readable format
    print(json.dumps(nested_dict, indent=4))

def check_scene_open():
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
