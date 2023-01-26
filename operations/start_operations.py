import pyautogui, time, tkinter
import tkinter
import os

from tkinter import filedialog, messagebox

def startup():
    print("")
    print("-------------------------------------------------------")
    print("-------------- Welcome to Scene Control ---------------")
    print("-------------------------------------------------------")
    print("")
    multiple_screens = input("Are you using multiple Screens ? (y/n):")
    print("")
    remote_access = input("Are you connected remotely ? (y/n):")
    print("")

    if multiple_screens == "y" and remote_access == "y":
        startup.setup = 1
    elif multiple_screens == "n" and remote_access == "y":
        startup.setup = 2
    elif multiple_screens == "y" and remote_access == "n":
        startup.setup = 3
    else:
        startup.setup = 4

    print("Setup Version:", startup.setup)
    print("")

def choose_directory():
    if startup.setup == 1:
        print("TBE")
        print("")
    elif startup.setup == 2:
        print("TBE")
        print("")
    elif startup.setup == 3:
        print("TBE")
        print("")
    else:
        directory = tkinter.filedialog.askdirectory()
        print("This is the selected location", scan_location)
        print("")
        print("These are the files present in the directory", os.listdir(scan_location))
        print("")

def create_arrays():
    """ Create array and assign default values """
    scans = 0
    processed = []
    registered = []
    aligned = []
    point_cloud = []
    exported = []

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
