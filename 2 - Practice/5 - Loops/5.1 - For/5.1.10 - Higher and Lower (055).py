# ======================================================================================================================
# CHALLENGE 55: Higher and Lower: Find them from a list of 5 values.
# ======================================================================================================================

"""
Challenge: 5.1.10 - Higher and Lower (055)
Category: 5 - Loops
Concepts Used:
    - for
    - range()
    - if()


Tags: for, range(), if(), import datetime, date.today().year
Status: ✔️ Completed
"""

higher = 0
lower = 0
for c in range (1, 6):
    weight = float(input('Type the weight of the {} participant: '.format(c)))
    if weight > higher:
        higher = weight
    if lower == 0 or lower > weight:
        lower = weight
print('\nHigher weight -> {:.2f}\nLower peso -> {:.2f}'.format(higher, lower))