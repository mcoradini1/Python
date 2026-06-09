# ======================================================================================================================
# CHALLENGE 49: Multiplication Table
# ======================================================================================================================

"""
Challenge: 5.1.4 - Multiplication Table (049)
Category: 5 - Loops
Concepts Used:
    - int()
    - for
    - range()

Tags: for, range(), print()
Status: ✔️ Completed
"""

n = int(input('Type the multiplication table that you need: '))
for c in range (1,11):
    print('{} * {} = {}'.format(c,n,c*n))