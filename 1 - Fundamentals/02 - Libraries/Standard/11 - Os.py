"""
OS — Python Standard Library

The os module provides functions 5.1 - For interacting with the operating system:
- listing files and directories
- creating and removing folders
- checking paths
- getting environment variables
- running system commands

This module demonstrates the most commonly used features.
"""

import os

# ---------------------------------------------------------
# LISTING FILES IN A DIRECTORY
# ---------------------------------------------------------

book_directory = "./"
print("Files in directory:", os.listdir(book_directory))

# ---------------------------------------------------------
# CHECKING IF A PATH EXISTS
# ---------------------------------------------------------

print(os.path.exists("os_examples.py"))
print(os.path.exists("nonexistent_file.txt"))

# ---------------------------------------------------------
# JOINING PATHS SAFELY
# ---------------------------------------------------------

folder = "example_folder"
filename = "data.txt"

full_path = os.path.join(folder, filename)
print("Joined path:", full_path)

# ---------------------------------------------------------
# CREATING AND REMOVING DIRECTORIES
# ---------------------------------------------------------

if not os.path.exists("demo_folder"):
    os.mkdir("demo_folder")      # create a folder
    print("Created folder: demo_folder")

if os.path.exists("demo_folder"):
    os.rmdir("demo_folder")      # remove empty folder
    print("Removed folder: demo_folder")

# ---------------------------------------------------------
# GETTING CURRENT WORKING DIRECTORY
# ---------------------------------------------------------

cwd = os.getcwd()
print("Current working directory:", cwd)

# ---------------------------------------------------------
# CHANGING DIRECTORIES
# ---------------------------------------------------------

# Example only — commented to avoid breaking execution
# os.chdir("..")
# print("Moved to:", os.getcwd())

# ---------------------------------------------------------
# ENVIRONMENT VARIABLES
# ---------------------------------------------------------

print("PATH variable:", os.environ.get("PATH"))
print("HOME variable:", os.environ.get("HOME"))

# ---------------------------------------------------------
# RUNNING SYSTEM COMMANDS
# ---------------------------------------------------------

# Example: list directory contents (platform dependent)
# os.system("dir")   # Windows
# os.system("ls")    # Linux / macOS

# ---------------------------------------------------------
# WALKING THROUGH A DIRECTORY TREE
# ---------------------------------------------------------

"""
os.walk() lets you iterate through all folders and files
inside a directory — useful 5.1 - For scanning projects.
"""

for root, dirs, files in os.walk("."):
    print("ROOT:", root)
    print("DIRS:", dirs)
    print("FILES:", files)
    break  # remove break to walk entire tree


