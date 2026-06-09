"""
LISTS — Python Fundamentals

- Ordered
- Mutable (changeable)
- Allow duplicates
- Indexable
- Defined with [] or list()
"""

# ---------------------------------------------------------
# CREATING LISTS
# ---------------------------------------------------------

a = []
b = list()
animals = ['bull', 'cow', 'lion']

# ---------------------------------------------------------
# ADDING ELEMENTS
# ---------------------------------------------------------

animals[2] = 'armadillo'       # replace element
animals.append('anteater')     # add to end
animals.insert(0, 'calf')      # insert at index 0

# ---------------------------------------------------------
# REMOVING ELEMENTS
# ---------------------------------------------------------

del animals[3]
animals.pop(3)
animals.pop()                  # remove last
animals.remove('bull')         # remove by value

# Safe remove
if 'cow' in animals:
    animals.remove('cow')

# ---------------------------------------------------------
# SORTING & LENGTH
# ---------------------------------------------------------

values = [1, 4, 5, 6, 9, 34, 9, 2]
values.sort()
values.sort(reverse=True)
print(len(values))

# ---------------------------------------------------------
# INDEX
# ---------------------------------------------------------

print(values.index(9))         # first occurrence

# ---------------------------------------------------------
# RANGE → LIST
# ---------------------------------------------------------

values = list(range(4, 11))    # [4..10]

# ---------------------------------------------------------
# LOOPING
# ---------------------------------------------------------

num = [2, 5, 9, 1]

for v in num:
    print(v)

for i, v in enumerate(num):
    print(i, v)

# ---------------------------------------------------------
# LIST ALIASING (BONDING)
# ---------------------------------------------------------

a = [2, 3, 4]
b = a
b[1] = 99
print(a, b)                    # both changed

# Correct copying
b = a[:]
m = list(a)

# ---------------------------------------------------------
# NESTED LISTS
# ---------------------------------------------------------

people = [['Peter', 25], ['Mary', 19]]
print(people[0][0])            # Peter

# ---------------------------------------------------------
# LIST COMPREHENSION
# ---------------------------------------------------------

squares = [n**2 for n in range(10)]
odds = [n for n in range(10) if n % 2 == 1]
