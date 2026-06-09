"""
COLLECTIONS — Python Standard Library

Provides specialized container datatypes:
- Counter
- defaultdict
- deque
- namedtuple
"""

from collections import Counter, defaultdict, deque, namedtuple

# ---------------------------------------------------------
# COUNTER
# ---------------------------------------------------------

c = Counter("banana")
print(c)

# ---------------------------------------------------------
# DEFAULTDICT
# ---------------------------------------------------------

d = defaultdict(int)
d["a"] += 1
print(d)

# ---------------------------------------------------------
# DEQUE
# ---------------------------------------------------------

dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)

# ---------------------------------------------------------
# NAMEDTUPLE
# ---------------------------------------------------------

Person = namedtuple("Person", "name age")
p = Person("Marlon", 31)
print(p.name, p.age)
