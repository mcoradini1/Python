"""
LAMBDA FUNCTIONS — Python Fundamentals (Mid)

Lambda functions are small anonymous functions.
Syntax:
    lambda arguments: expression

Used 5.1 - For:
- sorting
- filtering
- mapping
- quick inline functions
"""

# ---------------------------------------------------------
# BASIC LAMBDA
# ---------------------------------------------------------

square = lambda x: x * x
print(square(5))

# ---------------------------------------------------------
# LAMBDA WITH SORTING
# ---------------------------------------------------------

people = [
    ("Marlon", 31),
    ("Susana", 29),
    ("Anabela", 50)
]

people_sorted = sorted(people, key=lambda p: p[1])
print(people_sorted)

# ---------------------------------------------------------
# LAMBDA WITH MAP / FILTER
# ---------------------------------------------------------

nums = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))

print(doubled)
print(evens)
