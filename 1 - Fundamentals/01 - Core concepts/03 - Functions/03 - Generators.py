"""
GENERATORS — Python Fundamentals

Generators allow you to create iterators in a simple, memory-efficient way.
They use 'yield' instead of 'return'.

Benefits:
- Do not store entire sequences in memory
- Produce values on demand (lazy evaluation)
"""

# ---------------------------------------------------------
# BASIC GENERATOR
# ---------------------------------------------------------

def count_up_to(n):
    """Yield numbers from 1 to n."""
    num = 1
    while num <= n:
        yield num
        num += 1

for number in count_up_to(5):
    print(number)


# ---------------------------------------------------------
# GENERATOR EXPRESSIONS
# ---------------------------------------------------------

squares = (x*x for x in range(5))
print(next(squares))
print(list(squares))


# ---------------------------------------------------------
# INFINITE GENERATOR
# ---------------------------------------------------------

def infinite_counter():
    num = 0
    while True:
        yield num
        num += 1

# Example (be careful):
# 5.1 - For n in infinite_counter():
#     print(n)
