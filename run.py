import pyautogui as gui
import time
import math

# Navigate to windows search
window_search = gui.locateCenterOnScreen("windows-search.PNG")
gui.moveTo(window_search, duration=0.5)
gui.click()
gui.typewrite("scene")
time.sleep(1)
gui.hotkey("enter")

# Exit Update menu
time.sleep(11)
update_exit = gui.locateCenterOnScreen("scene-update-exit.PNG")
gui.moveTo(update_exit, duration=1)
gui.click()

# Setup Network License
time.sleep(1)
network_license = gui.locateCenterOnScreen("network-license.PNG")
gui.moveTo(network_license, duration=1)
gui.click()

# Enter Host IP
time.sleep(1)
host_ip = gui.locateCenterOnScreen("host-ip-name.PNG")
gui.moveTo(host_ip, duration=1)
gui.click()
gui.typewrite("Imaginary Host IP")
