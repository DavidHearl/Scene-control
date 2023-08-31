"""
Main file to run all the operations of automatic processing
in FARO SCENE software.
"""

from operations.start_operations import InitialProcedures


class MainApp:
    """ Docstring Placeholder """
    def run_operations(self):
        """ Docstring Placeholder """
        # Create an instance of the StartOperations class
        operations_instance = InitialProcedures()

        # Launches the program and gives the user a choice on which process option to select.
        operations_instance.startup()

        # Checks that Scene is open, if not, opens it.
        operations_instance.open_scene()

        # Clears the Update and Project transfer popup boxes.
        operations_instance.clear_popup_menus()

        # Gives the user the option to add a new project.
        processed_folder_path = operations_instance.set_folders()

        # Set the default folder that will be used in SCENE
        operations_instance.set_project_folder(processed_folder_path)

        # Import a project using the project transfer wizard
        # operations_instance.project_transfer()


# Create an instance of MainApp
app = MainApp()

# Run the operations
app.run_operations()
