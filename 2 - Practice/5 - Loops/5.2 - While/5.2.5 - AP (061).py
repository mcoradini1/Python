# ======================================================================================================================
# CHALLENGE 61: AP (061): Similar to 5.1.6 using FOR loop
# ======================================================================================================================

"""
Challenge: 5.2.5 - AP (061)
Category: 5 - Loops
Concepts Used:
    - while not


Tags: while not, range()
Status: ✔️ Completed
"""

t = int(input('Enter the first term '))
r = int(input('Enter the ratio '))

result = t
term_10th=0
while not term_10th == 11:
    print(result, end=' -> ')
    term_10th+=1
    result = result + r
print('END')