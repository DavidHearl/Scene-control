"""
Main file to run all the operations of automatic processing
in FARO SCENE software.
"""

from tkinter.filedialog import *
from operations.start_operations import *

# Create an instance of the StartOperations class
operations_instance = InitialProcedures()

# Call the instances
# operations_instance.startup()
# operations_instance.check_scene_open()
# operations_instance.folder_setup()
operations_instance.search_and_close()

# close_project()
# save_changes()
# wait_close()
# safe_zone()
# load_projects()

# print("All operations complete")

# # Count Number of files
# while more_files != False:
#     if scans < 12:
#         pyautogui.moveTo(600, (400 + (scans * 55)), duration=0.5)
#         time.sleep(1.25)
#     else:
#         pyautogui.scroll(-67, 600, 345 + (scans * 55))
#         time.sleep(1.75)

#     more_actions = pyautogui.locateOnScreen('items/more_actions.PNG')

#     if more_actions == None:
#         more_files = False
#     else:
#         scans += 1
#         print("Project Number:", scans)

# # Print Total number of projects
# safe_zone()
# print("Total Projects:", scans)

# # Set all job arrays to Fasle
# for i in range(scans):
#     processed.append(False)
#     registered.append(False)
#     point_cloud.append(False)
#     exported.append(False)

# for i in range(scans):
#     # Move mouse to project folder
#     if i < 11:
#         pyautogui.moveTo(600, (400 + (i * 55)), duration=0.5)
#         time.sleep(1)
#         pyautogui.click()
#     else:
#         safe_zone()
#         pyautogui.scroll(-67 * (i - 10), 600, 345 + ((i - 10) * 55))
#         time.sleep(1.75)
#         pyautogui.moveTo(600, (400 + (i * 55)), duration=0.5)
#         pyautogui.click()

#     wait_open()

#     # Check to see if operations have already been completed
#     processing_completed = pyautogui.locateOnScreen('items/processing-completed.PNG')
#     registration_completed = pyautogui.locateOnScreen('items/registration-completed.PNG')
#     point_cloud_completed = pyautogui.locateOnScreen('items/point-cloud-completed.PNG')

#     # Change value from False to True
#     if processing_completed != None:
#         processed[i+1] = True

#     if registration_completed != None:
#         registered[i+1] = True

#     if point_cloud_completed != None:
#         point_cloud[i+1] = True

#     print(processed[i+1], registered[i+1], point_cloud[i+1])

#     # Create point cloud
#     if processed[i+1] and registered[i+1] == True and point_cloud[i+1] == False:
#         # Click the create button
#         create_point_cloud = pyautogui.locateCenterOnScreen('items/create-point-cloud.PNG')
#         pyautogui.moveTo(create_point_cloud, duration=0.5)
#         pyautogui.click()
#         time.sleep(1)

#         # Configure Settings
#         pyautogui.moveTo(940, 330, duration=1)
#         pyautogui.dragTo(870, 330, duration=1, button='left')
#         pyautogui.moveTo(845, 385, duration=0.75)
#         pyautogui.click()
#         pyautogui.moveTo(860, 405, duration=0.5)
#         pyautogui.click()
#         ok_button = pyautogui.locateCenterOnScreen('items/ok-button.PNG')
#         pyautogui.moveTo(ok_button, duration=1)
#         pyautogui.click()
#         time.sleep(2)

#         point_cloud_in_progress = False
#         while point_cloud_in_progress == False:
#             point_cloud_processing = pyautogui.locateOnScreen('items/point-cloud-processing.PNG', confidence=0.9)
#             if point_cloud_processing == None:
#                 time.sleep(0.3)
#                 break

#         time.sleep(5)
#         ok_button = pyautogui.locateCenterOnScreen('items/ok-button.PNG', confidence=0.9)
#         pyautogui.moveTo(ok_button, duration=0.5)
#         point_cloud[i+1] = True

#     # Navigate to the close project button
#     close_project = pyautogui.locateCenterOnScreen('items/close-project.PNG')
#     pyautogui.moveTo(close_project, duration=1)
#     pyautogui.click()

#     wait_close()
