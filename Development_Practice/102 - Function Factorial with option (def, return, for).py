# ======================================================================================================================
# CHALLENGE 101: Function Factorial
# ======================================================================================================================

"""
Challenge: 7.6 - Function Vote (101)
Category: 7 - Collections
Concepts Used:


Tags: import datetime, date.today().year, if, elif, else
Status: ✔️ Completed
"""

def factorial(n, show=False):
    """

    :param n: Value to calculate factorial
    :param show: Show or not the calculation order
    :return: Sum of the values of n
    """

    f = 1
    for c in range(n,0,-1):
        if show: #WE START ASSUMING ITS TRUE
            print(c, end='')
            if c > 1:
                print(' x ', end = '')
            else:
                print(' = ', end = '')
        f *= c
    return f

print(factorial(5, False))
print(factorial(10, True))
print(help(factorial))

