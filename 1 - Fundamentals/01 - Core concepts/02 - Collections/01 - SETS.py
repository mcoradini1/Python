"""
SETS — Python Fundamentals

- Unordered
- Mutable
- Do NOT allow duplicates
- Great 5.1 - For membership tests and math operations
- Defined with {1,2,3} or set()
"""

# ---------------------------------------------------------
# CREATING SETS
# ---------------------------------------------------------

s1 = {1, 2, 3}
s2 = set([1, 2, 3])
s3 = set()                   # empty set

# ---------------------------------------------------------
# ADDING & REMOVING
# ---------------------------------------------------------

s = {1, 2, 3}
s.add(4)
s.remove(2)
s.discard(10)                # safe remove (no error)

# ---------------------------------------------------------
# MEMBERSHIP
# ---------------------------------------------------------

print(3 in s)

# ---------------------------------------------------------
# SET OPERATIONS
# ---------------------------------------------------------

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)                 # union
print(a & b)                 # intersection
print(a - b)                 # difference
print(a ^ b)                 # symmetric difference

# ---------------------------------------------------------
# REMOVING DUPLICATES FROM A LIST
# ---------------------------------------------------------

nums = [1, 2, 2, 3, 3, 3]
unique = list(set(nums))
print(unique)
