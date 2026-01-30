#DOCSTRING
#THESE ARE THE DOCUMENTATION STRINGS, EXAMPLE ON part 3.

#1 - TO PREPARE THE DOCSTRING WE NEED TO OPEN '3 QUOTATION MARKS' AND EVERYTHING WROTE INSIDE IT IS OUR DOCSTRING.
#2 - AFTER 3 QUOTATION MARKS I CAN PRESS ENTER, AND I WILL HAVE AN PRE-MODELED DOCSTRING TO FOLLOW

def test(a, b, c):
    """
    Inside here is the information about my function, kind of tips of how to use it.
    to access it, we just need to use the command help(test), to be able to read it.

    :param a: will be used in the sum
    :param b: will be used in the sum
    :param c: will be used in the sum
    :return: not set yet

    """

    d = a + b + c
    print(d)

test(1,2,3)
print('\n\n')
help(test)





