from git_hub_manager import *

def run_initial_gui():
    while True:
        # Print the menu options
        print("1. Run git_hub_manager")
        print("2. Quit")

        # Get the user's selection
        selection = input("Enter your selection: ")

        # Run the appropriate option
        if selection == "1":
            # Run the git_hub_manager
            run_git_manager()
        elif selection == "2":
            # Quit the program
            break
        else:
            # Invalid selection
            print("Invalid selection. Please try again.")
