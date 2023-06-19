import pyautogui
import time
import tkinter
import os
import json

class InitialProceedures:
    def __init__(self):
        self.operations = [
            "1: Processing & Registration",
            "2: Overview Map, Point Cloud Creation & Project Export",
            "3: Processing",
            "4: Registration",
            "5: Overview Map & Point Cloud Creation",
            "6: Recap Project Export"
        ]

    def startup(self):
        # Introduction
        print("")
        print("----------------------------------------------------------")
        print("---------- Welcome to Automatic Scan Processing ----------")
        print("----------------------------------------------------------")
        print("")

        print("Select which operation you would like to run ?")
        print("")

        # Prints list with a small delay
        for i in range(6):
            time.sleep(0.3)
            print(self.operations[i])

        print("")

        # Takes input from user, doesn't allow wrong input
        while True:
            print("Please enter the operation number you wish to run:")
            operation_result = input()

            if operation_result.isdigit():
                operation_number = int(operation_result)
                if 1 <= operation_number <= 6:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 6.")
            else:
                print("Invalid input. Please enter a number between 1 and 6.")

        # Prints confirmation of selected choice
        print("")
        print("You have selected operation", self.operations[operation_number - 1])
        print("")
        print("If this is not correct, press CTRL + C and restart the program")

        return operation_number

    def check_scene_open(self):
        print("Checking if SCENE is open...")
        print("")

        time.sleep(0.5)

        scene_open = pyautogui.locateCenterOnScreen("./items/scene-icon.PNG", confidence=0.9)
        if scene_open is None:
            print("Scene is NOT open, opening now...")
            print("")
            windows_search = pyautogui.locateCenterOnScreen("items/windows-search.PNG")
            pyautogui.moveTo(windows_search, duration=0.5)
            pyautogui.click()
            pyautogui.write('scene', interval=0.1)
            pyautogui.hotkey('enter')
            close_button = None
            while close_button is None:
                print("Waiting for Scene to load...")
                print("")
                time.sleep(3)
                close_button = pyautogui.locateCenterOnScreen("items/close.PNG")
                if close_button is not None:
                    break

            close = pyautogui.locateCenterOnScreen("items/close.PNG", confidence=0.9)
            pyautogui.moveTo(close, duration=1)
            pyautogui.click()
        else:
            print("Scene is already open...")
            print("")

    def folder_setup(self):
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
        print("Number of items: ", len(directory_content))
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

        print(json.dumps(nested_dict, indent=4))
