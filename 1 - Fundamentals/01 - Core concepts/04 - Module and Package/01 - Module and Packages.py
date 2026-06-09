"""
MODULES & PACKAGES — Python Fundamentals

Modules and packages help organise code into logical, reusable components.
They reduce complexity, improve readability, and make maintenance easier.

Python encourages modular programming by allowing you to split large programs
into smaller files (modules) and folders (packages).
"""

# ---------------------------------------------------------
# MODULES
# ---------------------------------------------------------
"""
A module is simply a Python file (.py) that contains functions, classes,
or variables. Any .py file can be imported as a module.

Examples of built-in modules:
    import math
    import random
    import datetime
"""

# Example: using a built-in module
import math
print(math.sqrt(25))     # 5.0
print(math.trunc(3.99))  # 3


# ---------------------------------------------------------
# IMPORTING FROM MODULES
# ---------------------------------------------------------

"""
Different ways to import:

1. import math
   - Access using math.function()

2. from math import sqrt
   - Access directly: sqrt(25)

3. from math import *
   - Imports everything (not recommended)

4. import my_module
   - Import your own module from the same folder
"""

from math import sqrt
print(sqrt(49)) #square root function


# ---------------------------------------------------------
# PACKAGES
# ---------------------------------------------------------
"""
A package is a folder containing multiple related modules.
A package must contain an __init__.py file (even if empty).

Example structure:

library/
│
├── strings.py
├── numbers.py
├── dates.py
├── colors.py
└── __init__.py

You can import modules from a package like this:
    from library import numbers
    from library.strings import format_name
"""

# Example (conceptual — requires actual package folder):
# from library import numbers
# from library.strings import clean_text


# ---------------------------------------------------------
# WHY USE MODULES & PACKAGES?
# ---------------------------------------------------------
"""
1. Reduce program complexity
2. Improve readability and organisation
3. Make maintenance easier
4. Promote code reuse
5. Enable team collaboration
6. Allow separation of concerns (each module handles one responsibility)
"""


# ---------------------------------------------------------
# CREATING YOUR OWN MODULES
# ---------------------------------------------------------
"""
To create your own module:

1. Create a file: mytools.py
2. Add functions inside it
3. Import it in another script:

    import mytools
    mytools.my_function()

Or:

    from mytools import my_function
"""

# Example (conceptual):
# File: mytools.py
# def greet(name):
#     print(f"Hello, {name}!")

# In another file:
# from mytools import greet
# greet("Marlon")


# ---------------------------------------------------------
# __init__.py AND PACKAGE INITIALISATION
# ---------------------------------------------------------
"""
The __init__.py file turns a folder into a package.
It can be empty, or it can define what gets imported by default.

Example __init__.py:

    from .numbers import add
    from .strings import clean

This allows:
    from library import add, clean
"""


# ---------------------------------------------------------
# GOOD PRACTICES
# ---------------------------------------------------------
"""
✔ Keep modules focused on one responsibility
✔ Use clear, descriptive names
✔ Avoid circular imports
✔ Avoid 'from module import *'
✔ Use packages 5.1 - For larger projects
✔ Keep __init__.py clean and intentional
"""


# ---------------------------------------------------------
# PREPARATION FOR PRACTICE
# ---------------------------------------------------------
"""
You will start using modules in Practice 16.
You will create your own modules in Practice 107.
"""
