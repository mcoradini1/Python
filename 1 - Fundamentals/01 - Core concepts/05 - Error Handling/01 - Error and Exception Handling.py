"""
ERROR HANDLING — Python Fundamentals

Python programs can fail due to:
- Syntax errors (incorrect code structure)
- Semantic errors (logic mistakes)
- Exceptions (runtime errors)

Exception handling allows programs to fail gracefully instead of crashing.

The try/except structure:
    try:
        # code that may fail
    except:
        # runs if an error occurs
    else:
        # runs if no error occurs (optional)
    finally:
        # always runs (optional)
"""

# ---------------------------------------------------------
# BASIC TRY / EXCEPT
# ---------------------------------------------------------

try:
    a = 10
    b = 0
    c = a / b
except:
    print("(EXAMPLE 1) Something went wrong.")
else:
    print("We are good.")
finally:
    print("(EXAMPLE 1) Bye bye\n")


# ---------------------------------------------------------
# CATCHING THE ERROR OBJECT
# ---------------------------------------------------------

try:
    a = 10
    b = 0
    c = a / b
except Exception as error:
    print(f"(EXAMPLE 2) Error message: {error}")
    print(f"(EXAMPLE 2) Error type: {error.__class__}")
else:
    print("We are good.")
finally:
    print("(EXAMPLE 2) Bye bye\n")


# ---------------------------------------------------------
# CATCHING A SPECIFIC ERROR
# ---------------------------------------------------------

try:
    a = 10
    b = 0
    c = a / b
except ZeroDivisionError:
    print("(EXAMPLE 3) We cannot divide by zero.")
else:
    print("We are good.")
finally:
    print("(EXAMPLE 3) Bye bye\n")


# ---------------------------------------------------------
# MULTIPLE EXCEPT BLOCKS
# ---------------------------------------------------------

try:
    a = int(input("Type first number: "))
    b = int(input("Type second number: "))
    c = a / b
except ZeroDivisionError:
    print("(ZeroDivisionError) Cannot divide by zero.")
except ValueError:
    print("(ValueError) Only integer numbers are allowed.")
except TypeError:
    print("(TypeError) Invalid type used in operation.")
except KeyboardInterrupt:
    print("\n(KeyboardInterrupt) User cancelled the input.")
else:
    print("We are good.")
finally:
    print("(EXAMPLE 4) Bye bye")


# ---------------------------------------------------------
# GOOD PRACTICES
# ---------------------------------------------------------
"""
✔ Catch specific exceptions whenever possible
✔ Avoid using a bare 'except:' unless absolutely necessary
✔ Use 'finally' 5.1 - For cleanup (closing files, releasing resources)
✔ Use 'else' 5.1 - For code that should run only when no error occurs
✔ Never hide errors silently — always log or print something meaningful
"""
