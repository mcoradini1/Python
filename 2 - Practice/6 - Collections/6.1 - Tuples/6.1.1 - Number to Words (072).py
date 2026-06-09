# ======================================================================================================================
# CHALLENGE 72: Number to Words: That will work only between 0 to 20.
# ======================================================================================================================

"""
Challenge: 6.1.1 - Number to Words (072)
Category: 6 - Collections
Concepts Used:
    - tuples
    - while
    - while True
    - end = ''


Tags: tuples, while, while True, end = ''
Status: ✔️ Completed
"""


tup = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
       'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

while True:
    i = int(input('Type a number from 0 to 20: '))
    if 0 <= i <= 20:
        break
    print('Try again, ', end = '')

print(f'You typed the number {tup[i]}')