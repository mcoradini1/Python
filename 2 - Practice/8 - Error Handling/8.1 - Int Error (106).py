# ======================================================================================================================
# CHALLENGE 107: Int Error: Check if the value typed is Integer
# ======================================================================================================================

"""
Challenge: 8.1 - Int Error (107)
Category: 8 - Error Handling
Concepts Used:


Tags: while True, try, except, continue, KeyboardInterrupt, else
Status: ✔️ Completed
"""


def isint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Entrance is not valid')
            continue
        except KeyboardInterrupt:
            print('User decide to terminate the program')
            return 0
        else:
            return n

n1 = isint('Type a number: ')
print(n1)