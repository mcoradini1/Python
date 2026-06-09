# ======================================================================================================================
# CHALLENGE 48: Odd (0 to 500): Show all the ODD numbers between 0 and 500.
# ======================================================================================================================

"""
Challenge: 5.1.3 - Odd (0 to 500) (048)
Category: 5 - Loops
Concepts Used:
    - for
    - range
    - print()
    - end = ''


Tags: for, range(), print(), end = ''
Status: ✔️ Completed
"""

sum_test = 0
count_test = 0
for c in range (0,501):
    if c%2 != 0 and c%3 == 0:
        sum_test = sum_test + c
        count_test = count_test + 1  #count_test+= 1
        print(sum_test, end=' ')
print('\n')
print(count_test)
