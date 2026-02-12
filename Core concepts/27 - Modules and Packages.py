'''
------------------------------------------------------------------------------------------------------------------------
Modules and Packages in Python
------------------------------------------------------------------------------------------------------------------------

Modules and packages are essential tools in Python for organizing and structuring code effectively.
Dividing a program into smaller parts helps:

1 - Reduce overall program complexity
2 - Improve readability and organization
3 - Make maintenance and updates easier
4 - Promote code reuse


------------------------------------------------------------------------------------------------------------------------
Modules
------------------------------------------------------------------------------------------------------------------------
In Python, any file with a .py extension can be considered a module.Each module typically contains related functions,
classes, or variables that represent a specific part of the system. By separating functionality into modules,
a program becomes more structured and easier to manage.

Example:
import math (It is a native module from python)

------------------------------------------------------------------------------------------------------------------------
Packages
------------------------------------------------------------------------------------------------------------------------

A package is a collection of related modules organized within a folder.
It helps structure larger projects by grouping related functionality together.

For example, imagine a package named library containing several modules:

library
│
├── strings.py
├──     __init__.py
├── numbers.py
├──     __init__.py
├── dates.py
├──    __init__.py
├── colors.py
├──    __init__.py
__init__.py


Example:
from library import numbers

'''
