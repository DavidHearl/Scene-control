import PySimpleGUI as sg

# Define the theme
sg.theme('Dark')

message = 'Checking scene is open'

# Define the layout
layout = [
    [sg.Text(message, font=('Helvetica', 16), justification='center', background_color='black', text_color='grey', pad=(2,2))],
    [sg.Checkbox('Processing')],
    [sg.Checkbox('Registration')],
    [sg.Checkbox('Overview Map')],
    [sg.Checkbox('Point Cloud')],
    [sg.Checkbox('RCS Export')],
    [sg.Checkbox('RCP Export')],
    [sg.Button('Submit')]
]

# Create the window
window = sg.Window('Automated Scan Processing', layout, size=(400, 400))

# Event loop to process events and get checkbox values
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Submit':
        # Access the checkbox values
        checkbox1_value = values[0]
        checkbox2_value = values[1]
        checkbox3_value = values[2]
        checkbox4_value = values[3]
        checkbox5_value = values[4]
        checkbox6_value = values[5]

        # Do something with the checkbox values
        print("Processing   :", checkbox1_value)
        print("Registration :", checkbox2_value)
        print("Overview Map :", checkbox3_value)
        print("Point Cloud  :", checkbox4_value)
        print("RCS Export   :", checkbox5_value)
        print("RCP Export   :", checkbox6_value)

# Close the window
window.close()
