import time
import tkinter
import os
import json
import psutil
import subprocess


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
                return

        print("The program is not open. Opening SCENE...")
        try:
            subprocess.Popen("C:\Program Files\FARO\SCENE\SCENE.exe")
        except Exception as e:
            print("Failed to open SCENE:", str(e))
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
                    time.sleep(2)  # Add a slight delay to the open confirmation message.
                    print("SCENE has been opened successfully.")
                    return

        print("Failed to open SCENE. Please check the installation.")

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

        print(json.dumps(nested_dict, indent=4))
