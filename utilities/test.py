# import tkinter as tk

# def button_click():
#     # Define the function to execute when the button is clicked
#     print("Button clicked!")

# # Create the main window
# window = tk.Tk()

# # Create a button widget
# button = tk.Button(window, text="Click Me!", command=button_click)

# # Add the button to the window
# button.pack()

# # Start the main event loop
# window.mainloop()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

def button_click():
    # Define the function to execute when the button is clicked
    print("Button clicked!")

# Create the application object
app = QApplication(sys.argv)

# Create the main window
window = QMainWindow()

# Create a button widget
button = QPushButton("Click Me!", window)
button.clicked.connect(button_click)

# Add the button to the window
window.setCentralWidget(button)

# Show the window
window.show()

# Run the application event loop
sys.exit(app.exec_())