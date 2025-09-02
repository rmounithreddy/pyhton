import os

def list_directory_contents(path="."):
    try:
        # List all files and directories in the given path
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to list contents of the current directory
list_directory_contents()
