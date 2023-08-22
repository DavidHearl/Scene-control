"""
Main file to run all the operations of automatic processing
in FARO SCENE software.
"""

from tkinter.filedialog import *
from operations.start_operations import *

# Create an instance of the StartOperations class
operations_instance = InitialProcedures()

# /////////////////////////////////////////////////////
# /// Calls the instances for each of the functions ///
# /////////////////////////////////////////////////////

# Launches the program and gives the option to choose which process you would like to complete.
operations_instance.startup()

# Checks that Scene is open, if not, opens it.
operations_instance.open_scene()

# Clears the Update and Project transfer popup boxes.
operations_instance.clear_popup_menus()

# Gives the user the option to add a new project.
operations_instance.import_project()

# operations_instance.validate_database()
