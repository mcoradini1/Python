# ======================================================================================================================
# CHALLENGE 50: Sum of EVEN: Sum all Evens in a specific range.
# ======================================================================================================================

"""
Challenge: 5.1.5 - Sum of EVEN (050)
Category: 5 - Loops
Concepts Used:
    - for
    - range()
    - if()
    - else()

Tags: for, range(), if(), else()
Status: ✔️ Completed
"""


sum_even = 0
count_odd = 0
for c in range(1, 7):
    n = int(input('Type the {} value '.format(c)))
    if n%2 == 0:
        sum_even = sum_even + n
    else:
        count_odd = count_odd + 1

print('\n\n{} EVENS \n{} ODDS \n{} SUM OF EVENS'.format(6 - count_odd, count_odd, sum_even))
