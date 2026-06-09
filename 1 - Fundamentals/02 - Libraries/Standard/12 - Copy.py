"""
COPY — Python Standard Library

Python variables do NOT store objects directly.
They store *references* to objects.

This means:
- assigning a list to another variable does NOT create a new list
- modifying one reference may affect the other

The copy module provides:
- copy.copy()      → shallow copy
- copy.deepcopy()  → deep copy

This module explains the difference.
"""

import copy

# ---------------------------------------------------------
# ASSIGNMENT (NO COPY)
# ---------------------------------------------------------
"""
Assignment does NOT create a new object.
Both variables point to the same list.
"""

a = [1, 2, 3]
b = a  # no copy

b[0] = 99
print("Assignment:")
print("a:", a)   # changed!
print("b:", b)
print("a is b:", a is b)  # True — same object

# ---------------------------------------------------------
# SHALLOW COPY (copy.copy)
# ---------------------------------------------------------
"""
Shallow copy creates a new outer object,
but does NOT copy nested objects.

Useful when:
- the list is flat (no nested lists)
- you only need a new container, not new inner objects
"""

x = [1, [2, 3, 4]]
y = copy.copy(x)

print("\nShallow copy:")
print("x:", x)
print("y:", y)
print("x is y:", x is y)  # False — new outer list
print("x[1] is y[1]:", x[1] is y[1])  # True — inner list shared

# modifying nested list affects both
y[1][0] = 999
print("After modifying y[1][0]:")
print("x:", x)
print("y:", y)

# ---------------------------------------------------------
# DEEP COPY (copy.deepcopy)
# ---------------------------------------------------------
"""
Deep copy creates:
- a new outer object
- AND new copies of all nested objects

Useful when:
- the object contains nested lists/dicts
- you want complete independence
"""

x = [1, [2, 3, 4]]
z = copy.deepcopy(x)

print("\nDeep copy:")
print("x:", x)
print("z:", z)
print("x is z:", x is z)          # False
print("x[1] is z[1]:", x[1] is z[1])  # False — inner list copied

# modifying nested list does NOT affect original
z[1][0] = 777
print("After modifying z[1][0]:")
print("x:", x)
print("z:", z)

# ---------------------------------------------------------
# SUMMARY
# ---------------------------------------------------------
"""
Assignment:
    a = b
    → both refer to the same object

Shallow copy:
    copy.copy()
    → new outer object
    → inner objects shared

Deep copy:
    copy.deepcopy()
    → new outer object
    → new inner objects
"""
