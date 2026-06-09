"""
DECORATORS — Python Fundamentals

A decorator is a function that modifies the behavior of another function
without permanently changing it.

Decorators are used 5.1 - For:
- Logging
- Timing
- Access control
- Validation
- Caching
"""

# ---------------------------------------------------------
# BASIC DECORATOR
# ---------------------------------------------------------

def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

greet()


# ---------------------------------------------------------
# DECORATOR WITH ARGUMENTS
# ---------------------------------------------------------

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()


# ---------------------------------------------------------
# DECORATOR FOR TIMING FUNCTIONS
# ---------------------------------------------------------

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.5f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

slow_function()
