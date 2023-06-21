import time
import tkinter
import os
import json
import psutil
import subprocess
import pytesseract
import pyautogui
import itertools


class InitialProcedures:
    def __init__(self):
        # Processing options to choose from
        self.operations = [
            "1: Processing & Registration",
            "2: Overview Map, Point Cloud Creation & Project Export",
            "3: Processing",
            "4: Registration",
            "5: Overview Map & Point Cloud Creation",
            "6: Recap Project Export"
        ]

        # Set Tesseract path
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def startup(self):
        # Introduction
        print("")
        print("----------------------------------------------------------")
        print("---------- Welcome to Automatic Scan Processing ----------")
        print("----------------------------------------------------------")
        print("")

        print("Select which operation you would like to run ?")
        print("")

        # Prints list of operations with a small delay
        for i in range(6):
            time.sleep(0.2)
            print(self.operations[i])

        # Adds a space to the terminal
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

        return operation_number

        # Prints confirmation of selected choice
        print("")
        print("You have selected operation", self.operations[operation_number - 1])
        print("")
        print("If this is not correct, press CTRL + C and restart the program")
        print("")

    def open_scene(self):
        # Prints statement with small delay
        print("Checking if SCENE is open...")
        time.sleep(0.5)
        print("")

        # Program name variable
        program_name = 'SCENE.exe'

        # Checks to see if the program is open
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == program_name:
                print("The program is open.")
                print("")
                return
        print("The program is not open. Opening SCENE...")
        print("")
        # If the program is not open then open it.
        try:
            subprocess.Popen('C:\Program Files\FARO\SCENE\SCENE.exe')
        except Exception as e:
            print("Failed to open SCENE:", str(e))
            print("")
            return

        # Keep checking if the program is open
        max_attempts = 10
        delay_between_attempts = 1
        attempts = 0

        # Define the spinning icons
        spinning_icons = ['-', '\\', '|', '/']

        # Loop through attempts
        while attempts < max_attempts:
            time.sleep(delay_between_attempts)
            attempts += 1

            # Check if the program is open
            for proc in psutil.process_iter(['name']):
                if proc.info['name'] == program_name:
                    # Create an iterator that cycles through the spinning icons
                    icon_cycle = itertools.cycle(spinning_icons)

                    # Loop through iterations
                    for _ in range(150):
                        # Get the next spinning icon from the iterator
                        spinning_icon = next(icon_cycle)
                        loading_message = f"Loading {spinning_icon}"
                        print(loading_message, end='\r')
                        time.sleep(0.05)

                    print("SCENE has been opened successfully.")
                    print("")
                    return

        # Print error message
        print("Failed to open SCENE. Please check the installation.")
        print("")

    def folder_setup(self):
        # Ask user to Select Directory
        print("Using the dialog box, please select the folder containing the scans")
        print("")
        directory = tkinter.filedialog.askdirectory()
        print("Selected Directory:", directory)
        print("")
        time.sleep(1)

        # Create an array
        outer_keys = []
        inner_keys = [
            'processed',
            'registered',
            'aligned',
            'clean_up',
            'point_cloud_creation',
            'point_cloud_export',
            'recap_export',
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

        # Print nested directory
        # print(json.dumps(nested_dict, indent=4))

    def search_and_close(self):
        # Capture screenshot
        screenshot = pyautogui.screenshot()
        # Perform OCR on the screenshot
        text = pytesseract.image_to_string(screenshot)

        target_text = "Updates and News"

        if target_text in text:
            print(f"Found '{target_text}' on the screen")

            # Find the position of the text "Close" using OCR
            try:
                text_location = pyautogui.locateOnScreen('items/close.png')
                if text_location is not None:
                    # Get the center coordinates of the text "Close"
                    text_position = pyautogui.center(text_location)
                    # Move the mouse to the position of the text "Close"
                    pyautogui.moveTo(text_position, duration="0.5")
                    # Perform a click action
                    pyautogui.click()
                    print("Clicked on 'Close'")
                    print("")
                else:
                    print("'Close' button not found")
            except Exception as e:
                print("Error occurred while locating 'Close' button:", str(e))

        else:
            print(f"'{target_text}' not found on the screen")
