# ======================================================================================================================
# CHALLENGE 47: Even (0 to 50): Show all the EVEN numbers between 0 and 50.
# ======================================================================================================================

"""
Challenge: 5.1.2 - Even (0 to 50) (047)
Category: 5 - Loops
Concepts Used:
    - for
    - range
    - print()
    - end = ''



Tags: for, range(), print(), end = ''
Status: ✔️ Completed
"""

for c in range (0, 52):
    if c%2 == 0:
        print(c, end=',')
print('\n')

for c in range (0, 51, 2):
    print(c, end=' ')
