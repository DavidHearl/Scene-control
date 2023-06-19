import time
import tkinter
import os
import json
import psutil
import subprocess
import pytesseract
import pyautogui

from PIL import Image
from tqdm import tqdm


class InitialProcedures:
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

        # Prints confirmation of selected choice
        print("")
        print("You have selected operation", self.operations[operation_number - 1])
        print("")
        print("If this is not correct, press CTRL + C and restart the program")
        print("")

        return operation_number

    def check_scene_open(self):
        print("Checking if SCENE is open...")
        print("")

        time.sleep(0.5)

        program_name = 'SCENE.exe'
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == program_name:
                print("The program is open.")
                print("")
                return

        print("The program is not open. Opening SCENE...")
        print("")
        try:
            subprocess.Popen("C:\Program Files\FARO\SCENE\SCENE.exe")
        except Exception as e:
            print("Failed to open SCENE:", str(e))
            print("")
            return

        # Wait for SCENE to open
        max_attempts = 10
        delay_between_attempts = 1
        attempts = 0
        while attempts < max_attempts:
            time.sleep(delay_between_attempts)
            attempts += 1

            # Check if SCENE is now open
            for proc in psutil.process_iter(['name']):
                if proc.info['name'] == program_name:
                    for _ in tqdm(range(100), desc="Loading", unit="%", ncols=80):
                        time.sleep(0.05)
                    print("")
                    print("SCENE has been opened successfully.")
                    print("")
                    return

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
        print(json.dumps(nested_dict, indent=4))

    # Set Tesseract path (replace with the correct path)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def search_and_close(self):
        screenshot = pyautogui.screenshot()  # Capture screenshot
        screenshot.show()
        text = pytesseract.image_to_string(screenshot)  # Perform OCR on the screenshot

        target_text = "Updates and News"

        if target_text in text:
            print(f"Found '{target_text}' on the screen")
            # Add code to find "Close" and move mouse to it and click
        else:
            print(f"'{target_text}' not found on the screen")
