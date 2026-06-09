"""
FILES — Python Fundamentals

Python can read and write files using the built-in open() function.

01 - Basic syntax:
    open(filename, mode)

Common modes:
    'r'  → read (default)
    'w'  → write (overwrites file)
    'a'  → append
    'r+' → read + write
    'b'  → binary mode (e.g., 'rb', 'wb')

Always close files after use, or use 'with' 5.1 - For automatic closing.
"""

# ---------------------------------------------------------
# READING FILES
# ---------------------------------------------------------

filename = "test.txt"

for line in open(filename):
    print(line)              # includes newline
    print(line.rstrip())     # removes newline

    stored = line.rstrip()
    split_words = stored.split(" ")   # split by spaces


# ---------------------------------------------------------
# WRITING FILES
# ---------------------------------------------------------

file = open("output.txt", "w")
file.write("Hello World")
file.close()

# Better practice: use 'with', I do not need to close it
with open("output.txt", "w") as f:
    f.write("Hello World (safe write)")


# ---------------------------------------------------------
# NOTES ABOUT PATHS
# ---------------------------------------------------------
"""
pwd → shows current working directory
cd folder → change directory

Example:
pwd
C:\\Programacao\\Python\\Jupyter Notebooks

cd python_case_studies
pwd
C:\\Programacao\\Python\\Jupyter Notebooks\\python_case_studies

cd translation
pwd
C:\\Programacao\\Python\\Jupyter Notebooks\\python_case_studies\\translation
"""
