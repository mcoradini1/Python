"""
ITERATORS — Python Fundamentals (Mid)

An iterator is an object that can be iterated (looped) over.
It implements two special methods:
    __iter__()
    __next__()

Python automatically creates iterators 5.1 - For lists, tuples, sets, dicts, etc.
"""

# ---------------------------------------------------------
# BASIC ITERATOR
# ---------------------------------------------------------

numbers = [1, 2, 3]
it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))

# ---------------------------------------------------------
# CUSTOM ITERATOR CLASS
# ---------------------------------------------------------

class CountUpTo:
    """Iterator that counts from 1 up to a limit."""

    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value
        raise StopIteration

for num in CountUpTo(5):
    print(num)
