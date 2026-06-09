"""
FUNCTIONS — Python Fundamentals

- Functions group reusable logic
- Always use parentheses when calling functions
- Use clear names and keep functions focused
- Python uses the LEGB scope model:
  L = Local
  E = Enclosing
  G = Global
  B = Built-in
"""

# ---------------------------------------------------------
# BASIC FUNCTIONS
# ---------------------------------------------------------

def show_hyphen():
    """Print a horizontal separator line."""
    print('-' * 60)

show_hyphen()
print("MIAU")
show_hyphen()


def message(msg):
    """Print a message surrounded by hyphens."""
    print('-' * 60)
    print(msg)
    print('-' * 60)

message("This will show the message between two lines of hyphens.")


# ---------------------------------------------------------
# FUNCTIONS WITH PARAMETERS
# ---------------------------------------------------------

def sum_numbers(a, b):
    """Print the sum of two numbers."""
    s = a + b
    print(f"A soma A + B é igual a {s}")

sum_numbers(4, 5)
sum_numbers(a=5, b=10)
sum_numbers(b=2, a=3)


# ---------------------------------------------------------
# VARIABLE-LENGTH ARGUMENTS (*args)
# ---------------------------------------------------------

def counter(*num):
    """Print all received numbers in sequence."""
    for value in num:
        print(value, end=' ')
    print("FIM!")

counter(2, 1, 4, 3)
counter(2, 3)
counter(8, 6, 0, 0, 0, 8, 4, 32)


# ---------------------------------------------------------
# WORKING WITH LISTS INSIDE FUNCTIONS
# ---------------------------------------------------------

def twice(lst):
    """Multiply each element of a list by 2 (in-place)."""
    for i in range(len(lst)):
        lst[i] *= 2

values = [7, 8, 8, 5, 7, 89]
twice(values)
print(values)


def soma2(*values):
    """Sum all values and show partial results."""
    s = 0
    for num in values:
        s += num
        print(f"Summing {num}, total is now {s}")


# ---------------------------------------------------------
# OPTIONAL / DEFAULT ARGUMENTS
# ---------------------------------------------------------

def function(a=0, b=0, c=0):
    """Demonstrate default parameters."""
    print(a)

function(a=1)


# ---------------------------------------------------------
# VARIABLE SCOPE (LEGB)
# ---------------------------------------------------------

y = 3            # global
global_x = 8     # global

def variables():
    """Demonstrate local vs global variables."""
    global global_x
    global_x = 9     # modifies global variable

    x = 3            # local
    y = 4            # local

    print(f"global_x (GLOBAL): {global_x}")
    print(f"x (LOCAL): {x}")
    print(f"y (LOCAL): {y}")

variables()
print(y)            # global y


# ---------------------------------------------------------
# RETURNING VALUES
# ---------------------------------------------------------

def sum_no_return(a=0, b=0, c=0):
    """Print the sum of three numbers."""
    s = a + b + c
    print(f"The sum is {s}")

sum_no_return(1, 5, 4)


def sum_with_return(a=0, b=0):
    """Return the sum of two numbers."""
    return a + b

r1 = sum_with_return(2, 3)
r2 = sum_with_return(3, 5)


# ---------------------------------------------------------
# FACTORIAL EXAMPLE
# ---------------------------------------------------------

def factorial(number=1):
    """Return the factorial of a number."""
    f = 1
    for c in range(number, 0, -1):
        f *= c
    return f

print(factorial(1), factorial(5))


# ---------------------------------------------------------
# EVEN OR ODD EXAMPLE
# ---------------------------------------------------------

def even_or_odd(a=0):
    """Return True if number is even, False if odd."""
    return a % 2 == 0

n = int(input("Type a number: "))
print("Even" if even_or_odd(n) else "Odd")


# ---------------------------------------------------------
# SCOPE — PRACTICAL EXAMPLE
# ---------------------------------------------------------

def update1():
    """Append 1 to global list x."""
    x.append(1)

x = [1, 1]


def update(n, x):
    """Modify local n and mutate list x."""
    n = 2
    x.append(4)
    print(f"update: n={n}, x={x}")

def main():
    n = 1
    x = [0, 1, 2, 3]
    print(f"main before: n={n}, x={x}")
    update(n, x)
    print(f"main after: n={n}, x={x}")

main()


# ---------------------------------------------------------
# DOCSTRINGS
# ---------------------------------------------------------

def test(a, b, c):
    """
    Example function demonstrating docstrings.

    :param a: first value
    :param b: second value
    :param c: third value
    :return: sum of a, b, and c
    """
    d = a + b + c
    print(d)

test(1, 2, 3)
help(test)
