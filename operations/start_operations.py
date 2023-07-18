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

        self.sorted_nested_dict = None
        self.projects = []

        # Set Tesseract path
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def startup(self):
        # Introduction
        print("")
        print("----------------------------------------------------------")
        print("---------- Welcome to Automatic Scan Processing ----------")
        print("----------------------------------------------------------", end='\n\n')
        print("Select which operation you would like to run ?", end='\n\n')

        # Prints list of operations with a small delay
        for i in range(6):
            time.sleep(0.15)
            print(self.operations[i])

        # Adds a space to the terminal
        print()

        # Takes input from user, doesn't allow wrong input
        while True:
            print("Please enter the operation number you wish to run:", end=" ")
            operation_result = input()
            print()
            if operation_result.isdigit():
                operation_number = int(operation_result)
                if 1 <= operation_number <= 6:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 6.", end='\n\n')
            else:
                print("Invalid input. Please enter a number between 1 and 6.", end='\n\n')

        return operation_number

        # Prints confirmation of selected choice
        print("You have selected operation", self.operations[operation_number - 1], end='\n\n')
        print("If this is not correct, press CTRL + C and restart the program", end='\n\n')

    def open_scene(self):
        # Prints statement with small delay
        print("Checking if SCENE is open...", end='\n\n')
        time.sleep(0.5)

        # Program name variable
        program_name = 'SCENE.exe'

        # Checks to see if the program is open
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == program_name:
                print("The program is open.", end='\n\n')
                return
        print("The program is not open. Opening SCENE...", end='\n\n')
        # If the program is not open then open it.
        try:
            subprocess.Popen('C:\Program Files\FARO\SCENE\SCENE.exe')
        except Exception as e:
            print("Failed to open SCENE:", str(e), end='\n\n')
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

                    print("SCENE has been opened successfully.", end='\n\n')
                    return

        # Print error message
        print("Failed to open SCENE. Please check the installation.", end='\n\n')

    def search_and_close(self):
        # Capture screenshot
        screenshot = pyautogui.screenshot()
        # Perform OCR on the screenshot
        text = pytesseract.image_to_string(screenshot)

        target_text = "Updates and News"

        if target_text in text:
            print(f"Found '{target_text}' on the screen", end='\n\n')

            # Find the position of the text "Close" using OCR
            try:
                text_location = pyautogui.locateOnScreen('./items/close.png')
                if text_location is not None:
                    # Get the center coordinates of the text "Close"
                    text_position = pyautogui.center(text_location)
                    # Move the mouse to the position of the text "Close"
                    pyautogui.moveTo(text_position, duration=0.5)
                    # Perform a click action
                    pyautogui.click()
                    print("Clicked on 'Close'", end='\n\n')
                else:
                    print("'Close' button not found", end='\n\n')
            except Exception as e:
                print("Error occurred while locating 'Close' button:", str(e), end='\n\n')

        else:
            print(f"'{target_text}' was not found on the screen", end='\n\n')

def set_database(self):
    while True:
        user_input = input("Is the current file path correct? (y/n): ")
        print()
        if user_input.lower() == 'y':
            # print("Obtaining current file path, please wait...", end='\n\n')
                # directory = "E:/Caribbean Princess - Processed/"
                # print("Selected Directory:", directory, end='\n\n')
                # time.sleep(1)
            break
        else:
            print("Using the dialog box, please select the folder containing the scans", end='\n\n')
            directory = tkinter.filedialog.askdirectory()
            print("Selected Directory:", directory, end='\n\n')
            time.sleep(1.5)

    # Create an array
    inner_keys = ['processed', 'registered', 'aligned', 'clean_up',
                  'point_cloud', 'point_cloud_export', 'recap_export', 'uploaded']
    inner_value = False

    # List all files in the directory
    directory_content = os.listdir(directory)
    print("Number of items: ", len(directory_content), end='\n\n')

    # Create a nested dictionary
    nested_dict = {
        project: {inner_key: inner_value for inner_key in inner_keys}
        for project in directory_content
    }

    # Sort the outer keys alphabetically
    sorted_projects = sorted(nested_dict.keys())

    # Create a new dictionary with sorted outer keys
    self.sorted_nested_dict = {project: nested_dict[project] for project in sorted_projects}


def validate_database(self):
    # Define location of colored band
    location_x = [380, 620, 850]
    location_y = 560

    # Define Colors to search for: Green, Orange, Red, Gray
    colors = [(0, 153, 105), (225, 160, 0), (220, 17, 28), (240, 240, 240)]

    for project_number in range(12):
        y_coords = 400 + (project_number * 55)
        pyautogui.moveTo(400, y_coords, duration=1)
        pyautogui.click()

        # Wait while project opens
        print('Waiting for project to open...', end='\n\n')
        while pyautogui.locateOnScreen('./items/close-project.png') is None:
            time.sleep(1)
        print("Close Project Open", end='\n\n')

        # Search locations
        processed_color = pyautogui.pixel(location_x[0], location_y)
        registration_color = pyautogui.pixel(location_x[1], location_y)
        point_cloud_color = pyautogui.pixel(location_x[2], location_y)

        # Check processed status
        current_project = next(iter(self.sorted_nested_dict))
        if processed_color == colors[0]:
            self.sorted_nested_dict[current_project]["processed"] = True

        # Check registration status
        if registration_color == colors[0]:
            self.sorted_nested_dict[current_project]["registered"] = True

        # Check point cloud status
        if point_cloud_color == colors[0]:
            self.sorted_nested_dict[current_project]["point_cloud"] = True

        # Find and click close project button
        image_location = pyautogui.locateOnScreen('./items/close-project.png')
        if image_location is not None:
            image_center = pyautogui.center(image_location)
            time.sleep(0.5)
            pyautogui.click(image_center)
            print("Image clicked!", end='\n\n')
        else:
            print("Image not found!", end='\n\n')

        # Wait while project closes
        while "Projects Overview" not in pytesseract.image_to_string(pyautogui.screenshot()):
            time.sleep(1)
        print("Text found: Projects Overview")
        time.sleep(0.2)

    # Print list with updated values
    sorted_values = list(self.sorted_nested_dict.values())
    for project, values in zip(self.sorted_nested_dict.keys(), sorted_values):
        print("Project:", project, end=" ")
        print(json.dumps(values, indent=4), end='\n\n')
        time.sleep(0.2)
