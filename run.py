import pyautogui as gui
import time
import math

def waste_time():
    R = 200
    (x,y) = gui.size()
    (X,Y) = gui.position(x/2,y/2)
    gui.moveTo(X+R,Y)

    for i in range(90):
        if i%6==0:
            gui.moveTo(X+R*math.cos(math.radians(i*4)),Y+R*math.sin(math.radians(i*4)))

# Navigate to windows search
window_search = gui.locateCenterOnScreen("windows-search.PNG")
gui.moveTo(window_search, duration=0.5)
gui.click()
gui.typewrite("scene")
time.sleep(1)
gui.hotkey("enter")

# Exit Update menu
for x in range(8):
    waste_time()

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
