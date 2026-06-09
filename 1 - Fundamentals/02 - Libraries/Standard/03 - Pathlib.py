"""
PATHLIB — Python Standard Library

Modern, object-oriented file system paths.
"""

from pathlib import Path

# ---------------------------------------------------------
# BASIC PATHS
# ---------------------------------------------------------

p = Path(".")
print(p.resolve())

# ---------------------------------------------------------
# ITERATING FILES
# ---------------------------------------------------------

for file in p.iterdir():
    print(file)

# ---------------------------------------------------------
# READING / WRITING FILES
# ---------------------------------------------------------

text_file = Path("example.txt")
text_file.write_text("Hello from pathlib!")
print(text_file.read_text())
