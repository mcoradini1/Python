"""
CONTEXT MANAGERS — Python Fundamentals (Mid)

Context managers handle setup and cleanup automatically.
Most common example: 'with open() as f'
"""

# ---------------------------------------------------------
# USING WITH FILES
# ---------------------------------------------------------

with open("example.txt", "w") as f:
    f.write("Hello from context manager!")

# ---------------------------------------------------------
# CUSTOM CONTEXT MANAGER (CLASS)
# ---------------------------------------------------------

class MyContext:
    def __enter__(self):
        print("Entering context...")
        return "Resource"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context...")
        return False  # propagate exceptions

with MyContext() as resource:
    print(resource)

# ---------------------------------------------------------
# CUSTOM CONTEXT MANAGER (DECORATOR)
# ---------------------------------------------------------

from contextlib import contextmanager

@contextmanager
def my_manager():
    print("Start")
    yield "Resource"
    print("End")

with my_manager() as r:
    print(r)
