""" Docstring Placeholder """
import time
import tkinter
import os
import subprocess
import itertools
import shutil
import psutil
import pytesseract
import pyautogui
# import json
from tqdm import tqdm


class InitialProcedures:
    """ Docstring Placeholder """
    def __init__(self):
        """ Docstring Placeholder """
        # Processing options to choose from
        self.operations = [
            "Processing & Registration",
            "Overview Map, Point Cloud Creation & Project Export",
            "Processing",
            "Registration",
            "Overview Map & Point Cloud Creation",
            "Recap Project Export"
        ]

        self.sorted_nested_dict = None
        self.projects = []

        # Set Tesseract path
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Give the user choices to choose from
    def startup(self):
        """ Docstring Placeholder """
        # Introduction
        print()
        print("----------------------------------------------------------")
        print("---------- Welcome to Automatic Scan Processing ----------")
        print("----------------------------------------------------------", end='\n\n')
        print("Select which operation you would like to run ?", end='\n\n')

        while True:
            # Prints list of operations with a small delay
            for i in range(6):
                time.sleep(0.15)
                print(f"{i + 1}: {self.operations[i]}")

            # Adds a space to the terminal
            print()

            # Asks for input
            print("Please enter the operation number you wish to run:", end=' ')
            operation_result = input()
            print()

            if operation_result.isdigit():
                operation_number = int(operation_result)
                if 1 <= operation_number <= 6:
                    print(f"Operation {operation_number}: {self.operations[operation_number - 1]}\n")
                    while True:
                        confirmation = input("Is this the correct selection? (yes/no): ")
                        print()
                        if confirmation.lower() == "yes":
                            return operation_number
                        elif confirmation.lower() == "no":
                            break
                        else:
                            print("Invalid input. Please enter 'yes' or 'no'.", end='\n\n')
                else:
                    print("Invalid input. Please enter a number between 1 and 6.", end='\n\n')
            else:
                print("Invalid input. Please enter a number between 1 and 6.", end='\n\n')

    def open_scene(self):
        """ Docstring Placeholder """
        print("----------------------------------------------------------")
        print("----------------------- Open Scene -----------------------")
        print("----------------------------------------------------------", end='\n\n')
        print("Checking if SCENE is open...", end='\n\n')

        # Program name variable
        program_name = 'SCENE.exe'

        # Checks to see if the program is open
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == program_name:
                print(f"{program_name} is already open.", end='\n\n')
                return
        print(f"{program_name} is not open. Opening {program_name}...", end='\n\n')
        # If the program is not open then open it.
        try:
            subprocess.Popen(r'C:\Program Files\FARO\SCENE\SCENE.exe')
        except Exception as exception:
            print(f"Failed to open {program_name}: {exception}\n")
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

                    print(f"{program_name} has been opened successfully.", end='\n\n')
                    return

        # Print error message
        print(f"Failed to open {program_name}. Please check the installation.", end='\n\n')

    def clear_popup_menus(self):
        """ Docstring Placeholder """
        # Capture screenshot
        screenshot = pyautogui.screenshot()
        # Perform OCR on the screenshot
        text = pytesseract.image_to_string(screenshot)

        target_texts = ["Updates and News", "Project Transfer"]

        for target_text in target_texts:
            if target_text in text:
                print(f"Found '{target_text}' on the screen", end='\n\n')

                # Find the position of the text "Close" or "No" using OCR
                button_text = "Close" if target_text == "Updates and News" else "No"
                try:
                    text_location = pyautogui.locateOnScreen(f'./items/{button_text.lower()}.png')
                    if text_location is not None:
                        # Get the center coordinates of the text "Close" or "No"
                        text_position = pyautogui.center(text_location)
                        # Move the mouse to the position of the text "Close" or "No"
                        pyautogui.moveTo(text_position, duration=0.5)
                        # Perform a click action
                        pyautogui.click()
                        print(f"Clicked on '{button_text}'", end='\n\n')
                    else:
                        print(f"'{button_text}' button not found", end='\n\n')
                except Exception as exception:
                    print(f"Error occurred while locating '{button_text}' button: {exception}\n")

            else:
                print(f"'{target_text}' was not found on the screen", end='\n\n')

    def import_project(self):
        """ Docstring Placeholder """
        print("----------------------------------------------------------")
        print("------------------- Project Management -------------------")
        print("----------------------------------------------------------", end='\n\n')
        # Ask the user if they would like to add a project
        response = input("Would you like to import a project? (yes/no): ").lower()
        print()
        if response == "yes":
            # Ask the user to select the SD card.
            print("Please select the SD card containing the Raw scan data", end='\n\n')
            sd_card = tkinter.filedialog.askdirectory()
            print("Selected Directory:", sd_card, end='\n\n')

            # Ask the user where they would like the data to be stored.
            print("Please select the directory you would like to store the data in", end='\n\n')
            directory = tkinter.filedialog.askdirectory()
            print("Selected Directory:", directory, end='\n\n')

            # Ask the user the name of the ship
            while True:
                ship_name = input("What is the name of the ship?: ")
                print()
                if any(c.isdigit() for c in ship_name):
                    print("Please enter only the ship name without numbers.", end="\n\n")
                else:
                    # Ask for confirmation
                    confirmation = input(f"Is the ship called '{ship_name}'? (yes/no): ")
                    print()
                    if confirmation.lower() == "yes":
                        break  # Exit the loop if the ship name is confirmed
                    elif confirmation.lower() == "no":
                        continue
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.", end="\n\n")

            # Ask if the user knows the contract number
            while True:
                knows_contract = input("Do you know the contract number? (yes/no): ")
                print()
                if knows_contract.lower() == "yes":
                    contract_number = input("Please enter the contract number: ")
                    print()
                    if contract_number.isdigit():
                        break  # Exit the loop if the contract number is entered
                    else:
                        print("Invalid contract number format. Please use numbers only.\n")
                elif knows_contract.lower() == "no":
                    contract_number = "XXX"
                    break  # Exit the loop if the contract number is set to 'XXX'
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.", end="\n\n")

            # Create raw folder and copy data
            raw_folder_name = f"{contract_number} - {ship_name} - Raw"
            raw_folder_path = os.path.join(directory, raw_folder_name)
            os.makedirs(raw_folder_path, exist_ok=True)

            # Get the total number of items to copy
            total_items = len(os.listdir(sd_card))

            # Initialize tqdm with the total number of items
            with tqdm(total=total_items, unit='item(s)', desc='Copying') as pbar:
                # Copy contents from source_directory to the newly created folder
                for item in os.listdir(sd_card):
                    source_item = os.path.join(sd_card, item)
                    destination_item = os.path.join(raw_folder_path, item)
                    if os.path.isdir(source_item):
                        shutil.copytree(source_item, destination_item)
                    else:
                        shutil.copy2(source_item, destination_item)
                    pbar.update(1)  # Update the progress bar

            print()
            print(f"Contents copied to: {raw_folder_path}", end="\n\n")

            # Create folders and copy data
            processed_folder_name = f"{contract_number} - {ship_name} - Processed"
            processed_folder_path = os.path.join(directory, processed_folder_name)
            os.makedirs(processed_folder_path, exist_ok=True)

            print(f"Processing folder Created: {processed_folder_path}", end="\n\n")

    # def validate_database(self):
    #     # Define location of colored band
    #     location_x = [380, 620, 850]
    #     location_y = 560

    #     # Define Colors to search for: Green, Orange, Red, Gray
    #     colors = [
    #       (0, 153, 105), (225, 160, 0),
    #       (220, 17, 28), (240, 240, 240)
    #     ]

    #     for project_number in range(12):
    #         y_coords = 400 + (project_number * 55)
    #         pyautogui.moveTo(400, y_coords, duration=1)
    #         pyautogui.click()

    #         # Wait while project opens
    #         print('Waiting for project to open...', end='\n\n')
    #         while pyautogui.locateOnScreen('./items/close-project.png') is None:
    #             time.sleep(1)
    #         print("Close Project Open", end='\n\n')

    #         # Search locations
    #         processed_color = pyautogui.pixel(location_x[0], location_y)
    #         registration_color = pyautogui.pixel(location_x[1], location_y)
    #         point_cloud_color = pyautogui.pixel(location_x[2], location_y)

    #         # Check processed status
    #         current_project = next(iter(self.sorted_nested_dict))
    #         if processed_color == colors[0]:
    #             self.sorted_nested_dict[current_project]["processed"] = True

    #         # Check registration status
    #         if registration_color == colors[0]:
    #             self.sorted_nested_dict[current_project]["registered"] = True

    #         # Check point cloud status
    #         if point_cloud_color == colors[0]:
    #             self.sorted_nested_dict[current_project]["point_cloud"] = True

    #         # Find and click close project button
    #         image_location = pyautogui.locateOnScreen('./items/close-project.png')
    #         if image_location is not None:
    #             image_center = pyautogui.center(image_location)
    #             time.sleep(0.5)
    #             pyautogui.click(image_center)
    #             print("Image clicked!", end='\n\n')
    #         else:
    #             print("Image not found!", end='\n\n')

    #         # Wait while project closes
    #         while "Projects Overview" not in pytesseract.image_to_string(pyautogui.screenshot()):
    #             time.sleep(1)
    #         print("Text found: Projects Overview")
    #         time.sleep(0.2)

    #     # Print list with updated values
    #     sorted_values = list(self.sorted_nested_dict.values())
    #     for project, values in zip(self.sorted_nested_dict.keys(), sorted_values):
    #         print("Project:", project, end=" ")
    #         print(json.dumps(values, indent=4), end='\n\n')
    #         time.sleep(0.2)
